from django.http import JsonResponse

from meals.interactors.storage_interfaces.storage_interface import StorageInterface
from meals.storages.storage_implementation import StorageImplementation


class SaveMealStatusInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def save_meal_status(self, meal_id:str, meal_status:str):

        meal_status= self.storage.save_meal_status( meal_id=meal_id, meal_status=meal_status)

        return meal_status


