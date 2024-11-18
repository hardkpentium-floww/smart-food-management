import json
from unittest.mock import create_autospec, patch, Mock
import pytest

from meals.interactors.get_meal_preference_interactor import GetMealPreferenceInteractor
from meals.interactors.login_interactor import LoginInteractor
from meals.interactors.logout_interactor import LogoutInteractor
from meals.interactors.storage_interfaces.storage_interface import StorageInterface
from meals.tests.factories.models import UserAccountFactory, UserFactory


class TestInteractor:
    @pytest.fixture
    def storage(self):
        storage = create_autospec(StorageInterface)
        return storage


    def test_get_meal_preference(self, storage):
        #Arrange
        interactor = GetMealPreferenceInteractor(storage=storage)
        user_id = "user_id"
        meal_id = "meal_id"
        meal_type = "meal_type"
        meal_preference = "meal_preference"

        storage.get_meal_preference.return_value = "meal_preference"

        #Act
        meal_preference_res = interactor.get_meal_preference(user_id=user_id, meal_id=meal_id, meal_type=meal_type)

        #Assert
        assert meal_preference ==  meal_preference_res

