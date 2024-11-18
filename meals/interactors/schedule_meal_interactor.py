from meals.exceptions.custom_exceptions import ItemNotFound, InvalidQuantity, InvalidDate, InvalidMealType
from meals.interactors.storage_interfaces.storage_interface import ScheduleMealDTO, StorageInterface


class ScheduleMealInteractor:
    def __init__(self, storage: StorageInterface):
        self.storage = storage


    def schedule_meal(self, schedule_meal_dto: ScheduleMealDTO):

        check = self.storage.validate_item_ids(item_ids=schedule_meal_dto.item_ids)
        if not check:
            raise ItemNotFound(check)

        check = self.storage.validate_quantities(quantities=schedule_meal_dto.full_meal_quantities)
        if not check:
            raise InvalidQuantity

        check = self.storage.validate_quantities(quantities=schedule_meal_dto.half_meal_quantities)
        if not check:
            raise InvalidQuantity

        check = self.storage.validate_date(date=schedule_meal_dto.date)
        if not check:
            raise InvalidDate

        check = self.storage.check_meal_type(meal_type=schedule_meal_dto.meal_type)
        if not check:
            raise InvalidMealType

        response = self.storage.schedule_meal(schedule_meal_dto=schedule_meal_dto)


        return response