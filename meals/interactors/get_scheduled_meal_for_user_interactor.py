from datetime import datetime

from meals.exceptions.custom_exceptions import MealNotScheduledException, UserMealDoesNotExist
from meals.interactors.storage_interfaces.storage_interface import StorageInterface
from meals_gql.meal.types.types import UserScheduledMeal


class GetScheduledMealForUserInteractor:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_scheduled_meal_for_user(self,date:datetime.date, user_id:str)->any:

        response = self.storage.get_scheduled_meal_for_user(date=date, user_id=user_id)

        if not response:
            raise UserMealDoesNotExist(user_id=user_id)

        return response