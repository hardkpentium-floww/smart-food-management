from datetime import datetime

from meals.exceptions.custom_exceptions import MealNotScheduledException
from meals.interactors.storage_interfaces.storage_interface import StorageInterface, AdminScheduledMealDTO
from meals_gql.enums import MealTypeEnum
from meals_gql.meal.types.types import MealNotScheduled


class GetScheduledMealByAdminInteractor:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_scheduled_meal_by_admin(self,date:datetime.date, meal_type:str)->AdminScheduledMealDTO:
        meal_id = self.storage.get_meal_id_by_date_and_meal_type(date=date, meal_type=meal_type)
        if not meal_id:
            raise MealNotScheduledException(date)

        scheduled_meal_dto = self.storage.get_scheduled_meal_by_admin(meal_id=meal_id, date=date, meal_type=meal_type)

        return scheduled_meal_dto