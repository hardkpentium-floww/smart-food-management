from meals.exceptions.custom_exceptions import InvalidMeal, InvalidUser
from meals.interactors.storage_interfaces.storage_interface import StorageInterface


class SaveMealStatusInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def save_meal_status(self, meal_id:str, meal_status:str, user_id:str)->str:

        meal_user_id = self.storage.get_meal_user_id(meal_id=meal_id)
        if meal_user_id != user_id:
            raise InvalidUser(user_id)

        meal_status= self.storage.save_meal_status( meal_id=meal_id, meal_status=meal_status)

        return meal_status


