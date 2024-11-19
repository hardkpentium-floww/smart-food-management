from django.http import JsonResponse

from meals.interactors.storage_interfaces.storage_interface import StorageInterface
from meals.storages.storage_implementation import StorageImplementation
from meals_gql.enums import MealStatusEnum


class SaveMealStatusInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def save_meal_status(self, meal_id:str, meal_status:MealStatusEnum)->str:

        meal_status= self.storage.save_meal_status( meal_id=meal_id, meal_status=meal_status.value)

        return meal_status


