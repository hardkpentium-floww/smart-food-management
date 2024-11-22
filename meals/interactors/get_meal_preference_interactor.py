from meals.exceptions.custom_exceptions import InvalidMeal
from meals.interactors.storage_interfaces.storage_interface import StorageInterface
from meals_gql.enums import MealTypeEnum


class GetMealPreferenceInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def get_user_meal_preference(self, user_id:str, meal_id:str, meal_type:str)->str:

        invalid_meal_id = self.storage.is_valid_meal_id(meal_id=meal_id)
        if invalid_meal_id:
            raise InvalidMeal(invalid_meal_id)

        is_valid_user_meal = self.storage.is_user_meal_valid(user_id=user_id, meal_type=meal_type, meal_id=meal_id)
        if not is_valid_user_meal:
            raise InvalidMeal(is_valid_user_meal)

        meal_preference= self.storage.get_user_meal_preference(user_id=user_id, meal_id=meal_id, meal_type=meal_type)

        return meal_preference


