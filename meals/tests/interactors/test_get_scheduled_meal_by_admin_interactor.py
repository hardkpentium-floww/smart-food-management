import json
from unittest.mock import create_autospec, patch, Mock
import pytest
from future.backports.datetime import datetime

from meals.exceptions.custom_exceptions import MealNotScheduledException
from meals.interactors.get_scheduled_meal_by_admin_interactor import GetScheduledMealByAdminInteractor
from meals.interactors.login_interactor import LoginInteractor
from meals.interactors.logout_interactor import LogoutInteractor
from meals.interactors.storage_interfaces.storage_interface import StorageInterface
from meals.tests.factories.models import UserAccountFactory, UserFactory


class TestInteractor:
    @pytest.fixture
    def storage(self):
        storage = create_autospec(StorageInterface)
        return storage

    def test_get_scheduled_meal_by_admin(self, storage):
        #arrange
        interactor = GetScheduledMealByAdminInteractor(storage=storage)
        date = datetime.now()
        meal_type = "meal_type"

        scheduled_meal_dto = "scheduled_meal_dto"

        storage.get_scheduled_meal_by_admin.return_value = scheduled_meal_dto

        #act
        scheduled_meal_dto_res = interactor.get_scheduled_meal_by_admin(date=date, meal_type=meal_type)

        #assert
        assert scheduled_meal_dto_res == scheduled_meal_dto

    def test_get_scheduled_meal_by_admin_with_no_meals(self, storage):
        # arrange
        interactor = GetScheduledMealByAdminInteractor(storage=storage)
        date = datetime.now()
        meal_type = "meal_type"

        scheduled_meal_dto = None
        storage.get_scheduled_meal_by_admin.return_value = scheduled_meal_dto

        # act
        with pytest.raises(MealNotScheduledException):
            scheduled_meal_dto_res = interactor.get_scheduled_meal_by_admin(date=date, meal_type=meal_type)

        # assert
        assert True

