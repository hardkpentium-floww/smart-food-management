import json
from unittest.mock import create_autospec, patch, Mock
import pytest

from meals.interactors.get_meal_status_interactory import GetMealStatusInteractor
from meals.interactors.login_interactor import LoginInteractor
from meals.interactors.logout_interactor import LogoutInteractor
from meals.interactors.storage_interfaces.storage_interface import StorageInterface
from meals.tests.factories.models import UserAccountFactory, UserFactory


class TestInteractor:
    @pytest.fixture
    def storage(self):
        storage = create_autospec(StorageInterface)
        return storage


    def test_get_meal_status(self, storage):
        interactor = GetMealStatusInteractor(storage=storage)
        meal_id = "meal_id"
        meal_status = "meal_status"

        storage.get_meal_status.return_value = "meal_status"

        meal_status_res = interactor.get_meal_status(meal_id=meal_id)

        assert meal_status ==  meal_status_res

