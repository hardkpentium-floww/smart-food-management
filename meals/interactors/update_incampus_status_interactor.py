from meals.exceptions.custom_exceptions import ItemNotFound, InvalidQuantity, InvalidDate
from meals.interactors.storage_interfaces.storage_interface import ScheduleMealDTO, StorageInterface


class UpdateIncampusStatusInteractor:
    def __init__(self, storage: StorageInterface):
        self.storage = storage


    def update_incampus_status(self, user_id:str, incampus_status:bool):

        response = self.storage.update_incampus_status(user_id=user_id, incampus_status=incampus_status)


        return response