import json
from unittest.mock import create_autospec, patch, Mock
import pytest

from meals.interactors.login_interactor import LoginInteractor
from meals.interactors.logout_interactor import LogoutInteractor
from meals.interactors.save_meal_status_interactor import SaveMealStatusInteractor
from meals.interactors.storage_interfaces.storage_interface import StorageInterface
from meals.tests.factories.models import UserAccountFactory, UserFactory


class TestInteractor:
    @pytest.fixture
    def storage(self):
        storage = create_autospec(StorageInterface)
        return storage


    def test_save_meal_status(self, storage):
        # Arrange
        interactor = SaveMealStatusInteractor(storage=storage)
        meal_id = "meal_id"
        meal_status = "meal_status"

        storage.save_meal_status.return_value = "meal_status"

        # Act
        meal_status_res = interactor.save_meal_status(meal_id=meal_id, meal_status=meal_status)

        #Assert
        assert meal_status_res == meal_status
