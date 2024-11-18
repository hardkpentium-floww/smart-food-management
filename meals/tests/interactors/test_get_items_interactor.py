import json
from unittest.mock import create_autospec, patch, Mock
import pytest
from sqlparse.utils import offset

from meals.exceptions.custom_exceptions import NoItemsFound
from meals.interactors.get_items_interactor import GetItemsInteractor
from meals.interactors.login_interactor import LoginInteractor
from meals.interactors.logout_interactor import LogoutInteractor
from meals.interactors.storage_interfaces.storage_interface import StorageInterface
from meals.tests.factories.models import UserAccountFactory, UserFactory


class TestInteractor:
    @pytest.fixture
    def storage(self):
        storage = create_autospec(StorageInterface)
        return storage



    def test_get_items(self, storage):
        #Arrange
        interactor = GetItemsInteractor(storage=storage)
        offset = 0
        limit = 100
        items_dto = "items_dto"
        storage.get_items.return_value = items_dto

        #act
        items_dto_res = interactor.get_items(offset=offset, limit=limit)

        #Assert
        assert items_dto_res == items_dto


    def test_get_items_with_no_items(self, storage):
        # Arrange
        interactor = GetItemsInteractor(storage=storage)
        offset = 0
        limit = 100
        items_dto = []
        storage.get_items.return_value = items_dto

        # act
        with pytest.raises(NoItemsFound):
            items_dto_res = interactor.get_items(offset=offset, limit=limit)

        # Assert
        assert True

