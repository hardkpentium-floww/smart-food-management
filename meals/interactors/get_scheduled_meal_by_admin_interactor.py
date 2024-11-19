from datetime import datetime

from meals.exceptions.custom_exceptions import MealNotScheduledException
from meals.interactors.storage_interfaces.storage_interface import StorageInterface, AdminScheduledMealDTO
from meals_gql.enums import MealTypeEnum


class GetScheduledMealByAdminInteractor:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_scheduled_meal_by_admin(self,date:datetime.date,meal_type:str)->AdminScheduledMealDTO:
        meal_id = self.storage.get_meal_id_by_date_and_meal_type(date=date, meal_type=meal_type)
        scheduled_meal_dto = self.storage.get_scheduled_meal_by_admin(meal_id=meal_id, date=date, meal_type=meal_type)

        if not scheduled_meal_dto:
            raise MealNotScheduledException(date)

        return scheduled_meal_dto