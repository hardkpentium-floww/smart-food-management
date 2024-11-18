from datetime import datetime

from meals.constants.enums import MealTypeChoices, AteMealStatusChoices, MealPreferenceTypeChoices

from meals.interactors.storage_interfaces.storage_interface import StorageInterface, AccessTokenDTO, RefreshTokenDTO, \
    ItemDTO, ScheduleMealDTO, MealItemDTO, AdminScheduledMealDTO, AddMealDTO
import uuid

from meals.models import UserMeal
from meals_gql.meal.types.types import AdminScheduledMeal, MealItem, UserScheduledMeal


class StorageImplementation(StorageInterface):

    def login(self, username: str, user_id: str, password: str):
        from datetime import datetime, timedelta
        from meals.interactors.storage_interfaces.storage_interface import AccessTokenDTO, RefreshTokenDTO
        access_token_str = str(uuid.uuid4())
        refresh_token_str = str(uuid.uuid4())
        expires = datetime.now() + timedelta(days=1)
        application_id = self.get_application_id(application_name="meals")
        is_admin = self.check_admin(user_id=user_id)

        access_token_dto = AccessTokenDTO(
            user_id=user_id,
            token=access_token_str,
            application_id=application_id,
            expires=expires,
            scope="read write",
        )

        access_token = self.create_access_token(access_token_dto=access_token_dto)

        refresh_token_dto = RefreshTokenDTO(
            user_id=user_id,
            refresh_token=refresh_token_str,
            access_token_id=access_token.id,
            application_id=application_id
        )

        refresh_token = self.create_refresh_token(refresh_token_dto=refresh_token_dto)

        user_login_response = {
                    "user_id": user_id,
                    "is_admin": is_admin,
                    "access_token": access_token_str,
                    "expires_in": expires,
                    "token_type": "Bearer",
                    "scope": "read write",
                    "refresh_token": refresh_token_str
                }

        return user_login_response

    def logout(self, user_id: str, access_token_str:str):
        from oauth2_provider.models import AccessToken, RefreshToken
        access_token = AccessToken.objects.get(user_id=user_id,token=access_token_str)
        refresh_token = RefreshToken.objects.get(user_id=user_id,access_token_id=access_token.id)
        self.expire_access_token(access_token_id=access_token.id)
        self.revoke_refresh_token(refresh_token_id=refresh_token.id)

    def check_admin(self, user_id: str):
        from meals.models.user import User
        check = User.objects.get(id=user_id).is_admin
        return check

    def validate_user(self, user_id: str):
        from meals.models.user import User
        check = User.objects.filter(id=user_id).exists()
        return check

    def validate_meal(self, meal_id: str):
        from meals.models.meal import Meal
        check = Meal.objects.filter(id=meal_id)

        return check

    def get_application_id(self, application_name: str):
        from oauth2_provider.models import Application
        return Application.objects.get(name=application_name).id


    def expire_access_token(self, access_token_id: str):
        from oauth2_provider.models import AccessToken
        from datetime import datetime
        access_token = AccessToken.objects.get(id=access_token_id)
        access_token.expires = datetime.now()
        access_token.save()
        return access_token

    def get_items(self,offset:int,limit:int):
        from meals.models.item import Item
        items = Item.objects.all()
        items = items[offset:offset+limit]

        item_dtos = [
            ItemDTO(
                id=item.id,
                name=item.name,
                category=item.category,
                base_size_unit=item.base_size_unit,
                serving_size_unit=item.serving_size_unit
            ) for item in items
        ]

        return item_dtos



    def revoke_refresh_token(self, refresh_token_id: str):
        from oauth2_provider.models import RefreshToken
        from datetime import datetime
        refresh_token = RefreshToken.objects.get(id=refresh_token_id)
        refresh_token.revoked = datetime.now()
        refresh_token.save()
        return refresh_token

    def get_user_acc(self,user_id:str):
        from ib_users.models import UserAccount
        user = UserAccount.objects.get(user_id=user_id)
        return user

    def get_user(self, username:str):
        from meals.models.user import  User
        user = User.objects.filter(name=username).first()
        return user

    def create_access_token(self, access_token_dto: AccessTokenDTO):
        from oauth2_provider.models import AccessToken
        access_token = AccessToken.objects.create(
            user_id = access_token_dto.user_id,
            token = access_token_dto.token,
            application_id = access_token_dto.application_id,
            expires = access_token_dto.expires,
            scope = access_token_dto.scope
        )

        return access_token

    def schedule_meal(self, schedule_meal_dto: ScheduleMealDTO):
        from meals.models.meal import Meal
        from meals.models.meal_item import MealItem

        meal = Meal.objects.filter(date__date=schedule_meal_dto.date.date(), meal_type=schedule_meal_dto.meal_type).first()

        if meal:
            meal_items= MealItem.objects.filter(meal_id=meal.id)

            idx_to_remove = []

            for item in meal_items:
                if item.item_id in schedule_meal_dto.item_ids:
                    item.full_meal_qty = schedule_meal_dto.full_meal_quantities[schedule_meal_dto.item_ids.index(item.item_id)]
                    item.half_meal_qty = schedule_meal_dto.half_meal_quantities[schedule_meal_dto.item_ids.index(item.item_id)]
                    item.save()
                    idx = schedule_meal_dto.item_ids.index(item.item_id)
                    idx_to_remove.append(idx)

                else:
                    item.delete()

            for idx in sorted(idx_to_remove, reverse=True):
                del schedule_meal_dto.item_ids[idx]
                del schedule_meal_dto.full_meal_quantities[idx]
                del schedule_meal_dto.half_meal_quantities[idx]

            for item_id in schedule_meal_dto.item_ids:
                MealItem.objects.create(
                            id=str(uuid.uuid4()),
                            meal_id=meal.id,
                            item_id=item_id,
                            full_meal_qty=schedule_meal_dto.full_meal_quantities[schedule_meal_dto.item_ids.index(item_id)],
                            half_meal_qty=schedule_meal_dto.half_meal_quantities[schedule_meal_dto.item_ids.index(item_id)]
                        )
        else:
            meal = Meal.objects.create(
                id=str(uuid.uuid4()),
                date=schedule_meal_dto.date,
                meal_type=schedule_meal_dto.meal_type,
            )

            for i in range(len(schedule_meal_dto.item_ids)):
                meal_item = MealItem.objects.create(
                    id=str(uuid.uuid4()),
                    meal_id=meal.id,
                    item_id=schedule_meal_dto.item_ids[i],
                    full_meal_qty=schedule_meal_dto.full_meal_quantities[i],
                    half_meal_qty=schedule_meal_dto.half_meal_quantities[i],
                )

        return meal.id



    def create_refresh_token(self, refresh_token_dto: RefreshTokenDTO):
        from oauth2_provider.models import RefreshToken
        refresh_token = RefreshToken.objects.create(
            user_id = refresh_token_dto.user_id,
            token = refresh_token_dto.refresh_token,
            application_id = refresh_token_dto.application_id,
            access_token_id = refresh_token_dto.access_token_id
        )
        return refresh_token


    def validate_item_ids(self, item_ids:[int]):
        from meals.models.item import Item

        for i in range(len(item_ids)):
            check = Item.objects.filter(id=item_ids[i]).exists()
            if not check:
                return item_ids[i]

        return True


    def validate_quantities(self, quantities:[int]):
        quantities = list(quantities)
        for i in range(len(quantities)):
            if quantities[i] < 0:
                return False

        return True

    def validate_date(self, date:datetime):
        if date < datetime.now():
            return False

        return True


    def get_scheduled_meal_by_admin(self, date: datetime, meal_type:str):
        from meals.models.meal import Meal
        from meals.models.meal_item import MealItem
        meal =  Meal.objects.get(date__date=date.date(), meal_type=meal_type)

        meal_items = MealItem.objects.filter(meal_id=meal.id)
        item_dtos = [
            MealItemDTO(
                id = meal_item.item.id,
                name = meal_item.item.name,
                full_meal_qty = meal_item.full_meal_qty,
                half_meal_qty = meal_item.half_meal_qty
            ) for meal_item in meal_items
        ]
        meal_dto = AdminScheduledMealDTO(
                date = date,
                meal_type = meal_type,
                items = item_dtos,
                meal_id = meal.id
            )


        return meal_dto

    def get_meal_status(self, meal_id:str):
        user_meal= UserMeal.objects.get(meal_id=meal_id)

        return user_meal.meal_status

    def save_meal_status(self, meal_id:str, meal_status:str):
        user_meal = UserMeal.objects.get(meal_id=meal_id)

        user_meal.meal_status = meal_status
        user_meal.save()

        return user_meal.meal_status


    def get_meal_preference(self, meal_id:str, user_id:str, meal_type:str):
        meal = UserMeal.objects.filter(user_id=user_id,meal_id=meal_id, meal_type=meal_type.value).first()

        return meal.meal_preference

    def check_meal_type(self, meal_type:str):
        if meal_type in MealTypeChoices.get_list_of_values():
            return True

        return False

    def check_meal_status(self, meal_status:str):
        if meal_status in AteMealStatusChoices.get_list_of_values():
            return True

        return False

    def check_meal_preference(self, meal_preference:str):
        if meal_preference in MealPreferenceTypeChoices.get_list_of_values():
            return True

        return False

    def add_meal_for_user(self, add_meal_dto: AddMealDTO):
        from meals.models.user_meal import UserMeal
        from meals.models.user_custom_meal_item import UserCustomMealItem

        user_meal = UserMeal.objects.create(
            id=str(uuid.uuid4()),
            user_id=add_meal_dto.user_id,
            meal_id=add_meal_dto.meal_id,
            meal_type=add_meal_dto.meal_type,
            meal_preference=add_meal_dto.meal_preference,
            meal_status=add_meal_dto.meal_status
        )


        for i in range(len(add_meal_dto.meal_items)):
            UserCustomMealItem.objects.create(
                id=str(uuid.uuid4()),
                user_meal_id=user_meal.id,
                item_id=add_meal_dto.meal_items[i].item_id,
                meal_qty=add_meal_dto.meal_items[i].quantity
            )

        return user_meal.id

    def update_incampus_status(self, user_id: str, incampus_status: bool):
        from meals.models.user import User
        User.objects.filter(id=user_id).update(in_campus=incampus_status)

        return "success"

    # def get_meals_for_date(self, date:datetime):
    #     from meals.models.meal import Meal
    #     meals = Meal.objects.filter(date__date=date.date())

    def get_scheduled_meal_for_user(self, user_id:str, date:datetime):
        from meals.models.user_meal import UserMeal as UserMealModel
        from meals.models.meal import Meal
        from meals.models.user_custom_meal_item import UserCustomMealItem
        from meals.models.meal_item import MealItem as MealItemModel
        from meals_gql.meal.types.types import UserMeal

        meals = Meal.objects.filter(date__date=date.date())
        user_meals_res = []

        for meal in meals:
            user_meals = UserMealModel.objects.filter(meal_id=meal.id, meal__date__date=date.date())

            if not user_meals.exists():
                return None

            for user_meal in user_meals:
                meal_items = UserCustomMealItem.objects.filter(user_meal_id=user_meal.id)

                items = []
                for meal_item in meal_items:
                    item = MealItemModel.objects.get(item_id=meal_item.item.id)
                    items.append(MealItem(
                        id=meal_item.item.id,
                        name=item.item.name,
                        full_meal_quantity=item.full_meal_qty,
                        half_meal_quantity=item.half_meal_qty,
                        custom_meal_quantity=meal_item.meal_qty
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










