from meals.exceptions.custom_exceptions import ItemNotFound
from meals.interactors.storage_interfaces.storage_interface import StorageInterface, ItemDTO
from typing import List

class GetItemsInteractor:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_paginated_items(self, offset:int, limit:int)->List[ItemDTO]:

        item_dtos = self.storage.get_paginated_items(offset=offset, limit=limit)

        if not item_dtos:
            raise ItemNotFound(item_ids=[])

        return item_dtos