from meals.exceptions.custom_exceptions import NoItemsFound
from meals.interactors.storage_interfaces.storage_interface import StorageInterface


class GetItemsInteractor:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_items(self,offset:int,limit:int):

        item_dtos = self.storage.get_items(offset=offset,limit=limit)

        if len(item_dtos) == 0:
            raise NoItemsFound

        return item_dtos