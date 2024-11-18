from django.http import JsonResponse

from meals.interactors.storage_interfaces.storage_interface import StorageInterface
from meals.storages.storage_implementation import StorageImplementation


class GetMealPreferenceInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_meal_preference(self, user_id:str, meal_id:str, meal_type:str):

        meal_preference= self.storage.get_meal_preference( user_id=user_id, meal_id=meal_id, meal_type=meal_type)

        return meal_preference


