from meals.exceptions.custom_exceptions import ItemNotFound, InvalidQuantity
from meals.interactors.storage_interfaces.storage_interface import StorageInterface, ItemDTO
from typing import List

class GetItemsInteractor:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_paginated_items(self, offset:int, limit:int)->List[ItemDTO]:

        invalid_quantities = self.storage.are_quantities_valid(quantities=[offset, limit])
        if invalid_quantities:
            raise InvalidQuantity(invalid_quantities)

        item_dtos = self.storage.get_paginated_items(offset=offset, limit=limit)

        if not item_dtos:
            raise ItemNotFound(item_ids=[])

        return item_dtos