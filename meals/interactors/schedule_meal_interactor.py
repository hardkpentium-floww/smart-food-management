from datetime import datetime

from meals.exceptions.custom_exceptions import ItemNotFound, InvalidQuantity, InvalidDate, InvalidMealType
from meals.interactors.storage_interfaces.storage_interface import ScheduleMealDTO, StorageInterface
from meals.models import MealItem
import uuid

class ScheduleMealInteractor:
    def __init__(self, storage: StorageInterface):
        self.storage = storage


    def schedule_meal(self, schedule_meal_dto: ScheduleMealDTO)->str:

        invalid_item_ids = self.storage.are_item_ids_valid(item_ids=schedule_meal_dto.item_ids)
        if invalid_item_ids:
            raise ItemNotFound(invalid_item_ids)

        invalid_quantities = self.storage.are_quantities_valid(quantities=schedule_meal_dto.full_meal_quantities)
        if invalid_quantities:
            raise InvalidQuantity(invalid_quantities)

        invalid_quantities = self.storage.are_quantities_valid(quantities=schedule_meal_dto.half_meal_quantities)
        if invalid_quantities:
            raise InvalidQuantity(invalid_quantities)

        invalid_date = schedule_meal_dto.date < datetime.now().date()
        if invalid_date:
            raise invalid_date

        meal_id = self.storage.get_meal_id_by_date_and_meal_type(date=schedule_meal_dto.date, meal_type=schedule_meal_dto.meal_type)
        if meal_id:
            self.storage.create_or_update_meal_items(schedule_meal_dto=schedule_meal_dto, meal_id=meal_id)

        else:
            meal_id = self.storage.create_meal(schedule_meal_dto=schedule_meal_dto)
            self.storage.create_or_update_meal_items(schedule_meal_dto=schedule_meal_dto, meal_id=meal_id)


        return meal_id