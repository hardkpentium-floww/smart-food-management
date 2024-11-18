from datetime import datetime

from meals.exceptions.custom_exceptions import MealNotScheduledException, UserMealDoesNotExist
from meals.interactors.storage_interfaces.storage_interface import StorageInterface


class GetScheduledMealForUserInteractor:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_scheduled_meal_for_user(self,date:datetime, user_id:str):

        response = self.storage.get_scheduled_meal_for_user(date=date, user_id=user_id)

        if response == None:
            raise UserMealDoesNotExist

        return response