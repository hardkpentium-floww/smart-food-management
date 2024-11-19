from unittest.mock import create_autospec, patch, Mock
import pytest

from meals.exceptions.custom_exceptions import ItemNotFound
from meals.interactors.get_items_interactor import GetItemsInteractor
from meals.interactors.storage_interfaces.storage_interface import StorageInterface


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
        storage.get_paginated_items.return_value = items_dto

        #act
        items_dto_res = interactor.get_paginated_items(offset=offset, limit=limit)

        #Assert
        assert items_dto_res == items_dto


    def test_get_items_with_no_items(self, storage):
        # Arrange
        interactor = GetItemsInteractor(storage=storage)
        offset = 0
        limit = 100
        items_dto = None
        storage.get_paginated_items.return_value = items_dto

        # act
        with pytest.raises(ItemNotFound):
            items_dto_res = interactor.get_paginated_items(offset=offset, limit=limit)

        # Assert
        assert True

