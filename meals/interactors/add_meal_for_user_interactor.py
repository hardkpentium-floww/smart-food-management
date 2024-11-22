from meals.exceptions.custom_exceptions import *
from meals.interactors.storage_interfaces.storage_interface import StorageInterface, AddMealDTO


class AddUserMealInteractor:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def add_meal_for_user(self, add_meal_dto: AddMealDTO, user_id:str) ->str:

        invalid_user_id = self.storage.is_valid_user_id(user_id=add_meal_dto.user_id)
        if invalid_user_id:
            raise InvalidUser(invalid_user_id)

        invalid_user_id = user_id==add_meal_dto.user_id
        if invalid_user_id:
            raise InvalidUser(user_id)

        meal_scheduling_valid = self.storage.is_meal_scheduling_valid(meal_type=add_meal_dto.meal_type.value, date=add_meal_dto.date)
        if not meal_scheduling_valid:
            raise MealNotScheduledException(add_meal_dto.date)

        invalid_meal_id = self.storage.is_valid_meal_id_with_date(meal_id=add_meal_dto.meal_id, date=add_meal_dto.date.date)
        if invalid_meal_id:
            raise InvalidMeal(invalid_meal_id)

        item_ids = [item.item_id for item in add_meal_dto.meal_items]
        invalid_item_ids = self.storage.are_item_ids_valid(item_ids=item_ids)
        if invalid_item_ids:
            raise ItemNotFound(invalid_item_ids)

        quantities = [meal_item.quantity for meal_item in add_meal_dto.meal_items]
        invalid_quantities = self.storage.are_quantities_valid(quantities=quantities)
        if invalid_quantities:
            raise InvalidQuantity(invalid_quantities)

        user_meal_id = self.storage.create_user_meal(add_meal_dto=add_meal_dto)
        self.storage.add_custom_meal_items(user_meal_id=user_meal_id, add_meal_dto=add_meal_dto)

        return user_meal_id


