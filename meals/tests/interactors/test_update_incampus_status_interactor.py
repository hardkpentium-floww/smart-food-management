import json
from unittest.mock import create_autospec, patch, Mock
import pytest

from meals.interactors.login_interactor import LoginInteractor
from meals.interactors.logout_interactor import LogoutInteractor
from meals.interactors.storage_interfaces.storage_interface import StorageInterface
from meals.interactors.update_incampus_status_interactor import UpdateIncampusStatusInteractor
from meals.tests.factories.models import UserAccountFactory, UserFactory


class TestInteractor:
    @pytest.fixture
    def storage(self):
        storage = create_autospec(StorageInterface)
        return storage


    def test_update_incampus_status(self, storage):
        # Arrange
        interactor = UpdateIncampusStatusInteractor(storage=storage)
        user_id = "user_id"
        incampus_status = True

        storage.update_incampus_status.return_value = "success"
        # Act
        res = interactor.update_incampus_status(user_id=user_id, incampus_status=incampus_status)

        #Assert
        assert res == "success"


