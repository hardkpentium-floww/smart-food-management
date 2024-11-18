import json
from unittest.mock import create_autospec, patch, Mock
import pytest

from meals.interactors.login_interactor import LoginInteractor
from meals.interactors.logout_interactor import LogoutInteractor
from meals.interactors.storage_interfaces.storage_interface import StorageInterface
from meals.tests.factories.models import UserAccountFactory, UserFactory


class TestInteractor:
    @pytest.fixture
    def storage(self):
        storage = create_autospec(StorageInterface)
        return storage



    def test_logout(self, storage):
        #arrange
        interactor = LogoutInteractor(storage=storage)

        storage.logout.return_value = None

        expected_logout_response = {
            "status_code": 200,
            "res_status": "LOGOUT SUCCESS",
            "response": {
                "message": "logged out successfully"
            }
        }

        # Act
        response = interactor.logout(user_id="user_id", access_token="access_token")
        response_data = json.loads(response.content.decode('utf-8'))
        logout_response = response_data



        #Assert
        assert logout_response["status_code"] == expected_logout_response["status_code"]
        assert logout_response["res_status"] == expected_logout_response["res_status"]
        assert logout_response["response"]["message"] == expected_logout_response["response"]["message"]

