from datetime import datetime

from meals.exceptions.custom_exceptions import MealNotScheduledException
from meals.interactors.storage_interfaces.storage_interface import StorageInterface


class GetMealStatusInteractor:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_meal_status(self,meal_id:str)->str:

        invalid_meal_id = self.storage.is_valid_meal_id(meal_id=meal_id)
        if invalid_meal_id:
            raise MealNotScheduledException(invalid_meal_id)

        meal_status = self.storage.get_meal_status(meal_id=meal_id)


        return meal_status