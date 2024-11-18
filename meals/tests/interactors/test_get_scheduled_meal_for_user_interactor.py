import json
from unittest.mock import create_autospec, patch, Mock
import pytest
from future.backports.datetime import datetime

from meals.exceptions.custom_exceptions import UserMealDoesNotExist
from meals.interactors.get_scheduled_meal_for_user_interactor import GetScheduledMealForUserInteractor
from meals.interactors.login_interactor import LoginInteractor
from meals.interactors.logout_interactor import LogoutInteractor
from meals.interactors.storage_interfaces.storage_interface import StorageInterface
from meals.tests.factories.models import UserAccountFactory, UserFactory


class TestInteractor:
    @pytest.fixture
    def storage(self):
        storage = create_autospec(StorageInterface)
        return storage


    def test_get_scheduled_meal_for_user(self, storage):
        interactor = GetScheduledMealForUserInteractor(storage=storage)
        date = datetime.now()
        user_id = "user_id"

        response = "response"
        storage.get_scheduled_meal_for_user.return_value = response

        res = interactor.get_scheduled_meal_for_user(user_id=user_id, date=date)

        assert res == response

    def test_get_scheduled_meal_for_user_with_no_user_meals(self, storage):
        interactor = GetScheduledMealForUserInteractor(storage=storage)
        date = datetime.now()
        user_id = "user_id"
        response = None
        storage.get_scheduled_meal_for_user.return_value = response

        with pytest.raises(UserMealDoesNotExist):
            interactor.get_scheduled_meal_for_user(user_id=user_id, date=date)

        assert True

