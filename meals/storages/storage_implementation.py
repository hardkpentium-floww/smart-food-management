from datetime import datetime

from ib_users.models import UserAccount
from typing import List

from meals.interactors.storage_interfaces.storage_interface import StorageInterface, AccessTokenDTO, SessionTokensDTO, \
    ItemDTO, ScheduleMealDTO, MealItemDTO, AdminScheduledMealDTO, AddMealDTO
import uuid

from meals.models import UserMeal
from meals_gql.meal.types.types import AdminScheduledMeal, MealItem, UserScheduledMeal


class StorageImplementation(StorageInterface):

    def logout(self, user_id: str, access_token_str:str):
        from oauth2_provider.models import AccessToken, RefreshToken
        access_token_id = AccessToken.objects.filter(user_id=user_id,token=access_token_str).values("id").first()
        refresh_token_id = RefreshToken.objects.filter(user_id=user_id,access_token_id=access_token_id).values("id").first()
        return access_token_id, refresh_token_id


    def check_admin(self, user_id: str)->bool:
        from meals.models.user import User
        check= User.objects.get(id=user_id).values("is_admin")
        return check[0]["is_admin"]

    def is_password_valid(self, user_id:str, password:str)->bool:
        user_acc = UserAccount.objects.get(user_id=user_id)
        return user_acc.check_password(password)

    def is_valid_user_id(self, user_id: str)->bool|str:
        from meals.models.user import User
        check = User.objects.filter(id=user_id).exists()
        if not check:
            return user_id

    def is_valid_meal_id(self, meal_id: str)->bool|str:
        from meals.models.meal import Meal
        check = Meal.objects.filter(id=meal_id)

        if not check:
            return meal_id

    def get_application_id(self, application_name: str)->int:
        from oauth2_provider.models import Application
        app_id = Application.objects.filter(name=application_name).values("id").first()
        return app_id


    def expire_access_token(self, access_token_id: str)->None:
        from oauth2_provider.models import AccessToken
        from datetime import datetime
        access_token = AccessToken.objects.get(id=access_token_id)
        access_token.expires = datetime.now()
        access_token.save()

    def get_paginated_items(self, offset:int, limit:int)->List[ItemDTO]:
        from meals.models.item import Item
        items = Item.objects.all()
        sorted(items, key=lambda item: item.id)
        items = items[offset:offset+limit]

        item_dtos = [
            ItemDTO(
                item_id=item.id,
                name=item.name,
                category=item.category,
                base_size_unit=item.base_size_unit,
                serving_size_unit=item.serving_size_unit
            ) for item in items
        ]

        return item_dtos



    def revoke_refresh_token(self, refresh_token_id: str)->None:
        from oauth2_provider.models import RefreshToken
        from datetime import datetime
        refresh_token = RefreshToken.objects.get(id=refresh_token_id)
        refresh_token.revoked = datetime.now()
        refresh_token.save()

    def get_user_acc(self,user_id:str) -> UserAccount:
        from ib_users.models import UserAccount
        user_acc = UserAccount.objects.get(user_id=user_id)
        #return user acc obj since need to use the check password method of user acc obj
        return user_acc

    def get_user_id(self, username:str)->str:
        from meals.models.user import  User
        user_id = User.objects.filter(name=username).values("id").first()
        return user_id

    def create_access_token(self, access_token_dto: AccessTokenDTO)->str:
        from oauth2_provider.models import AccessToken
        access_token = AccessToken.objects.create(
            id = access_token_dto.access_token_id,
            user_id = access_token_dto.user_id,
            token = access_token_dto.token,
            application_id = access_token_dto.application_id,
            expires = access_token_dto.expires,
            scope = access_token_dto.scope
        )

        return access_token.id

    def create_meal(self,schedule_meal_dto:ScheduleMealDTO):
        from meals.models import Meal
        meal = Meal.objects.create(
            id=str(uuid.uuid4()),
            date=schedule_meal_dto.date,
            meal_type=schedule_meal_dto.meal_type,
        )

        return meal.id

    def get_meal_id_by_date_and_meal_type(self,date:datetime.date,meal_type:str):
        from meals.models import Meal
        meal_id = Meal.objects.filter(date__date=date,meal_type=meal_type).values("id").first()
        return meal_id



    def create_or_update_meal_items(self, schedule_meal_dto: ScheduleMealDTO, meal_id: str):
        from django.db import transaction
        meal_items = MealItem.objects.filter(meal_id=meal_id)

        items_to_update = []
        items_to_create = []
        existing_item_ids = []

        idx_to_remove = []

        for item in meal_items:
            if item.item_id in schedule_meal_dto.item_ids:
                idx = schedule_meal_dto.item_ids.index(item.item_id)
                item.full_meal_qty = schedule_meal_dto.full_meal_quantities[idx]
                item.half_meal_qty = schedule_meal_dto.half_meal_quantities[idx]
                items_to_update.append(item)
                idx_to_remove.append(idx)
                existing_item_ids.append(item.item_id)
            else:
                item.delete()

        for idx in sorted(idx_to_remove, reverse=True):
            del schedule_meal_dto.item_ids[idx]
            del schedule_meal_dto.full_meal_quantities[idx]
            del schedule_meal_dto.half_meal_quantities[idx]

        for idx, item_id in enumerate(schedule_meal_dto.item_ids):
            items_to_create.append(MealItem(
                id=str(uuid.uuid4()),
                meal_id=meal_id,
                item_id=item_id,
                full_meal_qty=schedule_meal_dto.full_meal_quantities[idx],
                half_meal_qty=schedule_meal_dto.half_meal_quantities[idx]
            ))

        with transaction.atomic():
            if items_to_update:
                MealItem.objects.bulk_update(items_to_update, ["full_meal_qty", "half_meal_qty"])
            if items_to_create:
                MealItem.objects.bulk_create(items_to_create)


    def create_refresh_token(self, refresh_token_dto: SessionTokensDTO)->str:
        from oauth2_provider.models import RefreshToken
        refresh_token = RefreshToken.objects.create(
            id = refresh_token_dto.refresh_token_id,
            user_id = refresh_token_dto.user_id,
            token = refresh_token_dto.refresh_token,
            application_id = refresh_token_dto.application_id,
            access_token_id = refresh_token_dto.access_token_id
        )
        return refresh_token.id


    def are_item_ids_valid(self, item_ids:[int]) -> List[str]:
        from meals.models.item import Item
        valid_item_ids = set(Item.objects.filter(id__in=item_ids).values_list('id', flat=True))
        invalid_ids = [item_id for item_id in item_ids if item_id not in valid_item_ids]
        if invalid_ids:
            return invalid_ids



    def are_quantities_valid(self, quantities:List[int])->List[int]:

        invalid_quantities = []
        for i in range(len(list(quantities))):
            if quantities[i] < 0:
                invalid_quantities.append(quantities[i])

        if len(invalid_quantities) >0 :
            return invalid_quantities



    def get_scheduled_meal_by_admin(self, meal_id:str,date:datetime.date,meal_type:str)->AdminScheduledMealDTO:
        from meals.models.meal_item import MealItem
        meal_items = MealItem.objects.filter(meal_id=meal_id)
        item_dtos = [
            MealItemDTO(
                meal_item_id = meal_item.item.id,
                name = meal_item.item.name,
                full_meal_qty = meal_item.full_meal_qty,
                half_meal_qty = meal_item.half_meal_qty
            ) for meal_item in meal_items
        ]
        meal_dto = AdminScheduledMealDTO(
                date = date,
                meal_type = meal_type,
                items = item_dtos,
                meal_id = meal_id
            )


        return meal_dto

    def get_meal_status(self, meal_id:str)->str:
        user_meal= UserMeal.objects.get(meal_id=meal_id)

        return user_meal.meal_status

    def save_meal_status(self, meal_id:str, meal_status:str)->str:
        user_meal = UserMeal.objects.get(meal_id=meal_id)

        user_meal.meal_status = meal_status
        user_meal.save()

        return user_meal.meal_status


    def get_user_meal_preference(self, meal_id:str, user_id:str, meal_type:str)->str:
        meal = UserMeal.objects.filter(user_id=user_id,meal_id=meal_id, meal_type=meal_type).first()

        return meal.meal_preference

    def create_user_meal(self, add_meal_dto: AddMealDTO)->str:
        user_meal = UserMeal.objects.create(
            id=str(uuid.uuid4()),
            user_id=add_meal_dto.user_id,
            meal_id=add_meal_dto.meal_id,
            meal_type=add_meal_dto.meal_type,
            meal_preference=add_meal_dto.meal_preference,
            meal_status=add_meal_dto.meal_status
        )

        return user_meal.id

    def add_custom_meal_items(self,user_meal_id:str, add_meal_dto: AddMealDTO)->str:
        from meals.models.user_custom_meal_item import UserCustomMealItem

        UserCustomMealItems=[UserCustomMealItem(
            id=str(uuid.uuid4()),
            user_meal_id=user_meal_id,
            item_id=meal_item.item_id,
            meal_qty=meal_item.quantity
        ) for meal_item in add_meal_dto.meal_items]

        UserCustomMealItem.objects.bulk_create(UserCustomMealItems)

        return user_meal_id

    def update_incampus_status(self, user_id: str, incampus_status: bool):
        from meals.models.user import User
        User.objects.filter(id=user_id).update(in_campus=incampus_status)
        message = "update incampus status success"
        return message


    def get_scheduled_meal_for_user(self, user_id:str, date:datetime.date)->UserScheduledMeal:
        from meals.models.user_meal import UserMeal as UserMealModel
        from meals.models.meal import Meal
        from meals.models.user_custom_meal_item import UserCustomMealItem
        from meals.models.meal_item import MealItem as MealItemModel
        from meals_gql.meal.types.types import UserMeal

        meals= Meal.objects.filter(date__date=date).values("id","meal_type")
        user_meals_res = []

        for meal in meals:
            user_meals = UserMealModel.objects.filter(meal_id=meal.id, meal__date__date=date)

            if not user_meals.exists():
                return None

            for user_meal in user_meals:
                meal_items = UserCustomMealItem.objects.filter(user_meal_id=user_meal.id)

                items = []
                item_ids = [meal_item.item.id for meal_item in meal_items]
                item_objs = MealItemModel.objects.filter(item_id__in=item_ids)

                for idx in range(len(meal_items)):
                    items.append(MealItem(
                        id=meal_items[idx].item.id,
                        name=item_objs[idx].item.name,
                        full_meal_quantity=item_objs[idx].full_meal_qty,
                        half_meal_quantity=item_objs[idx].half_meal_qty,
                        custom_meal_quantity=item_objs[idx].meal_qty
                    ))

                user_meals_res.append(UserMeal(
                        meal_type=meal.meal_type,
                        meal_id=meal.id,
                        meal_preference=user_meal.meal_preference,
                        items=items
                    ))


        return UserScheduledMeal(
            date=date,
            meals=user_meals_res
        )










