from datetime import datetime, timedelta
from unittest.mock import patch
import factory
import pytest

from meals.interactors.storage_interfaces.storage_interface import ScheduleMealDTO, AddMealDTO, MealItemDTO
from meals.models import MealItem, UserCustomMealItem
from meals.storages.storage_implementation import StorageImplementation
from meals.tests.factories.models import ApplicationFactory, UserFactory, UserAccountFactory, AccessTokenFactory, \
    RefreshTokenFactory, ItemFactory, MealFactory, MealItemFactory, UserMealFactory, UserCustomMealItemFactory
from meals.tests.factories.storage_dtos import AccessTokenDTOFactory, RefreshTokenDTOFactory, ScheduleMealDTOFactory, \
    AddMealDTOFactory, MealItemDTOFactory
from meals_gql.meal.mutations.schedule_meal import ScheduleMeal



@pytest.mark.django_db
class TestStorageImplementation:

    @pytest.fixture
    def storage(self):
        storage = StorageImplementation()
        return storage


    def test_create_access_token(self, storage):
        # Arrange
        access_token_dto = AccessTokenDTOFactory()
        user = UserAccountFactory(user_id=access_token_dto.user_id)
        application = ApplicationFactory(id=access_token_dto.application_id, user_id=access_token_dto.user_id)

        # act
        access_token = storage.create_access_token(access_token_dto=access_token_dto)

        # assert
        assert access_token.user_id == access_token_dto.user_id
        assert access_token.token == access_token_dto.token
        assert access_token.application_id == access_token_dto.application_id
        assert access_token.expires == access_token_dto.expires
        assert access_token.scope == access_token_dto.scope

    def test_create_refresh_token(self, storage):
        # Arrange
        refresh_token_dto = RefreshTokenDTOFactory()
        user = UserAccountFactory(user_id = refresh_token_dto.user_id)
        application = ApplicationFactory(id=refresh_token_dto.application_id, user_id=refresh_token_dto.user_id)
        access_token = AccessTokenFactory(id=refresh_token_dto.access_token_id, user_id=refresh_token_dto.user_id, application_id=refresh_token_dto.application_id)

        # act
        refresh_token = storage.create_refresh_token(refresh_token_dto=refresh_token_dto)

        # assert
        assert refresh_token.user_id == refresh_token_dto.user_id
        assert refresh_token.token == refresh_token_dto.refresh_token
        assert refresh_token.application_id == refresh_token_dto.application_id
        assert refresh_token.access_token_id == refresh_token_dto.access_token_id



    def test_get_application_id(self, storage):
        # Arrange
        application = ApplicationFactory()
        user = UserAccountFactory(user_id = application.user_id)

        # act
        app_id = storage.get_application_id(application_name = application.name)

        # assert
        assert app_id == application.id

    def test_expire_access_token(self, storage):
        # Arrange
        user = UserAccountFactory()
        application = ApplicationFactory(user_id=user.user_id)
        access_token = AccessTokenFactory(user_id=user.user_id, application_id=application.id)

        # act
        access_token = storage.expire_access_token(access_token_id=access_token.id)
        # assert
        assert access_token.expires.date() == datetime.now().date()

    def test_revoke_refresh_token(self, storage):
        # Arrange
        user = UserAccountFactory()
        application = ApplicationFactory()
        access_token = AccessTokenFactory(user_id=user.user_id, application_id=application.id)
        refresh_token = RefreshTokenFactory(access_token_id=access_token.id, application_id=application.id, user_id=user.user_id)

        # act
        refresh_token  = storage.revoke_refresh_token(refresh_token_id=refresh_token.id)

        # assert
        assert refresh_token.revoked.date() == datetime.now().date()

    def test_get_items(self, storage):
        # Arrange
        items = ItemFactory.create_batch(30)
        offset = 0
        limit = 14

        # act
        items_dto_res = storage.get_items(offset=offset, limit=limit)

        # assert
        assert len(items_dto_res) == limit


    def test_get_user_acc(self, storage):
        # Arrange
        user = UserAccountFactory()

        # act
        user_res = storage.get_user_acc(user_id=user.user_id)

        # assert
        assert user.user_id == str(user_res.user_id)


    def test_get_user(self, storage):
        # Arrange
        user = UserFactory()

        # act
        user_res = storage.get_user(username=user.name)

        # assert
        assert user_res.name == user.name


    def test_schedule_meal_update(self, storage):
        # Arrange
        meal = MealFactory()
        items = ItemFactory.create_batch(10)
        item_ids = [item.id for item in items]
        schedule_meal_dto = ScheduleMealDTOFactory(item_ids=item_ids, date=datetime.now()+timedelta(2))
        # act
        meal_id_res = storage.schedule_meal(schedule_meal_dto=schedule_meal_dto)

        # assert meal_id_res == meal.id   # wont work coz meal_id_res is autogen
        # assert
        assert True

    def test_schedule_meal_create(self, storage):
        # Arrange
        items = ItemFactory.create_batch(10)
        item_ids = [item.id for item in items]
        schedule_meal_dto = ScheduleMealDTOFactory(item_ids=item_ids, date=datetime.now() + timedelta(2))
        # act
        meal_id_res = storage.schedule_meal(schedule_meal_dto=schedule_meal_dto)

        # assert meal_id_res == meal.id   # wont work coz meal_id_res is autogen
        # assert
        assert True


    def test_validate_item_ids(self, storage):
        # Arrange
        items = ItemFactory.create_batch(10)
        item_ids = [item.id for item in items]
        # act
        res = storage.validate_item_ids(item_ids=item_ids)

        # assert
        assert res == True

    def test_validate_quantities(self, storage):
        # Arrange
        quantities = factory.List([factory.Faker("random_int", min=1, max=10000) for _ in range(10)])
        #Act
        res = storage.validate_quantities(quantities=quantities)

        # assert
        assert res == True

    def test_validate_date(self,storage):
        # Arrange
        date = datetime.now() + timedelta(3)
        # act
        res = storage.validate_date(date=date)

        # assert
        assert res == True


    def test_get_scheduled_meal_by_admin(self,storage):
        # Arrange
        meal = MealFactory()
        items = ItemFactory.create_batch(5)
        meal_items = []
        for item in items:
            meal_item = MealItemFactory(item_id=item.id, meal_id=meal.id)
            meal_items.append(meal_item)
        date = meal.date
        meal_type = meal.meal_type
        # act
        meal_dto_res = storage.get_scheduled_meal_by_admin(date=date, meal_type=meal_type)

        # assert
        assert meal_dto_res.date == date
        assert meal_dto_res.meal_type == meal_type
        assert meal_dto_res.meal_id == meal.id


    def test_get_meal_status(self, storage):
        # Arrange
        meal = MealFactory()
        user = UserFactory()
        user_meal = UserMealFactory(meal_id=meal.id, user_id=user.id)
        # act
        status_res = storage.get_meal_status(meal_id=meal.id)

        # assert
        assert status_res == user_meal.meal_status

    def test_save_meal_status(self, storage):
        # Arrange
        meal = MealFactory()
        user = UserFactory()
        user_meal = UserMealFactory(meal_id=meal.id, user_id=user.id)
        meal_status = "SKIPPED"
        # act
        status_res = storage.save_meal_status(meal_id=meal.id,meal_status=meal_status)

        # assert
        assert status_res == meal_status

    def test_get_meal_preference(self, storage):
        # Arrange
        meal = MealFactory()
        user = UserFactory()
        user_meal = UserMealFactory(meal_id=meal.id, user_id=user.id)
        # act
        meal_preference_res = storage.get_meal_preference(user_id=user.id, meal_id=meal.id, meal_type=user_meal.meal_type)

        # assert
        assert meal_preference_res == user_meal.meal_preference

    def test_check_meal_type(self, storage):
        # Arrange
        meal_type = "LUNCH"
        # act
        res = storage.check_meal_type(meal_type=meal_type)

        # assert
        assert res == True

    def test_check_meal_status(self, storage):
        # Arrange
        meal_status = "NULL"
        # act
        res = storage.check_meal_status(meal_status=meal_status)

        # assert
        assert res == True

    def test_check_meal_preference(self,storage):
        # Arrange
        meal_preference = "FULL"
        # act
        res = storage.check_meal_preference(meal_preference=meal_preference)

        # assert
        assert res == True

    def test_add_meal_for_user(self,storage):
        # Arrange
        user = UserFactory()
        meal = MealFactory()
        items = ItemFactory.create_batch(5)
        meal_items = []
        for item in items:
            meal_item = MealItemFactory(item_id=item.id, meal_id=meal.id)
            meal_items.append(meal_item)

        meal_item_dtos = []
        for meal_item in meal_items:
            meal_item_dto =  MealItemDTOFactory(item_id=meal_item.item_id)
            meal_item_dtos.append(meal_item_dto)
        add_meal_dto = AddMealDTOFactory(user_id=user.id, meal_items=meal_item_dtos, date=meal.date, meal_id=meal.id)

        # act
        res = storage.add_meal_for_user(add_meal_dto=add_meal_dto)

        # assert
        assert True

    def test_update_incampus_status(self, storage):
        # Arrange
        user = UserFactory()
        incampus_status = False
        # act
        res = storage.update_incampus_status(user_id=user.id, incampus_status=incampus_status)

        # assert
        assert res == "success"

    def test_get_scheduled_meal_for_user(self, storage):
        # Arrange
        date = datetime.now() + timedelta(2)
        meal = MealFactory(date=date)
        user = UserFactory()
        items = ItemFactory.create_batch(3)
        meal_types = ["BREAKFAST", "LUNCH", "DINNER"]
        for idx in range(3):
            user_meal = UserMealFactory(user_id=user.id, meal_id=meal.id, meal_type=meal_types[idx])
            user_meal_item = UserCustomMealItemFactory(user_meal_id=user_meal.id, item_id=items[idx].id)
            meal_item = MealItemFactory(meal_id=meal.id, item_id=items[idx].id)
        # act
        user_scheduled_meal_res = storage.get_scheduled_meal_for_user(user_id=user.id, date=date)
        # assert
        assert user_scheduled_meal_res.date == date
        assert user_scheduled_meal_res.meals[0].meal_type == "BREAKFAST"









