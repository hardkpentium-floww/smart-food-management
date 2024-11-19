from meals.exceptions.custom_exceptions import InvalidMeal
from meals.interactors.storage_interfaces.storage_interface import StorageInterface
from meals_gql.enums import MealTypeEnum


class GetMealPreferenceInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_user_meal_preference(self, user_id:str, meal_id:str, meal_type:MealTypeEnum)->str:

        invalid_meal_id = self.storage.is_valid_meal_id(meal_id=meal_id)
        if invalid_meal_id:
            raise InvalidMeal(invalid_meal_id)

        meal_preference= self.storage.get_user_meal_preference(user_id=user_id, meal_id=meal_id, meal_type=meal_type.value)

        return meal_preference


