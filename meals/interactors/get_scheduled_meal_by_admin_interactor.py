from datetime import datetime

from meals.exceptions.custom_exceptions import MealNotScheduledException
from meals.interactors.storage_interfaces.storage_interface import StorageInterface


class GetScheduledMealByAdminInteractor:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_scheduled_meal_by_admin(self,date:datetime,meal_type:str):

        scheduled_meal_dto = self.storage.get_scheduled_meal_by_admin(date=date, meal_type=meal_type)

        if scheduled_meal_dto == None:
            raise MealNotScheduledException

        return scheduled_meal_dto