from meals.exceptions.custom_exceptions import InvalidMealType, InvalidMealStatus, InvalidMealPreference, ItemNotFound, \
    InvalidQuantity, InvalidUser, InvalidMeal
from meals.interactors.storage_interfaces.storage_interface import StorageInterface, AddMealDTO


class AddMealForUserInteractor:
    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def add_meal_for_user(self, add_meal_dto: AddMealDTO):

        check = self.storage.validate_user(user_id=add_meal_dto.user_id)
        if not check:
            raise InvalidUser

        check = self.storage.validate_meal(meal_id=add_meal_dto.meal_id)
        if not check:
            raise InvalidMeal

        check = self.storage.check_meal_type(meal_type=add_meal_dto.meal_type)
        if not check:
            raise InvalidMealType

        check = self.storage.check_meal_status(meal_status=add_meal_dto.meal_status)
        if not check:
            raise InvalidMealStatus

        check = self.storage.check_meal_preference(meal_preference=add_meal_dto.meal_preference)
        if not check:
            raise InvalidMealPreference

        check = self.storage.validate_item_ids(item_ids=[item.item_id for item in add_meal_dto.meal_items])
        if check != True:
            raise ItemNotFound(check)

        check = self.storage.validate_quantities(quantities=[meal_item.quantity for meal_item in add_meal_dto.meal_items])
        if not check:
            raise InvalidQuantity

        user_meal_id = self.storage.add_meal_for_user(add_meal_dto=add_meal_dto)

        return user_meal_id