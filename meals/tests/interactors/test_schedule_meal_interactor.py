import json
from datetime import datetime
from unittest.mock import create_autospec, patch, MagicMock
import pytest
from future.backports.datetime import timedelta

from meals.exceptions.custom_exceptions import ItemNotFound, InvalidQuantity, InvalidDate
from meals.interactors.schedule_meal_interactor import ScheduleMealInteractor
from meals.interactors.storage_interfaces.storage_interface import StorageInterface, ScheduleMealDTO



class TestInteractor:
    @pytest.fixture
    def storage(self):
        storage = create_autospec(StorageInterface)
        return storage


    def test_schedule_meal(self, storage):
        # arrange
        interactor = ScheduleMealInteractor(storage=storage)
        schedule_meal_dto = MagicMock()
        schedule_meal_dto.date = datetime.now().date() + timedelta(2)
        meal_id = "meal_id"
        storage.are_item_ids_valid.return_value = None
        storage.are_quantities_valid.return_value = None
        storage.schedule_meal.return_value = meal_id
        storage.get_meal_id_by_date_and_meal_type.return_value = meal_id
        storage.create_or_update_meal_items.return_value = None
        storage.create_meal.return_value = meal_id

        # act
        response = interactor.schedule_meal(schedule_meal_dto=schedule_meal_dto)

        #assert
        assert response == meal_id

    def test_schedule_meal_with_invalid_item_id(self, storage):
        # arrange
        interactor = ScheduleMealInteractor(storage=storage)
        schedule_meal_dto = MagicMock()
        meal_id = "meal_id"
        storage.are_item_ids_valid.return_value = True
        storage.are_quantities_valid.return_value = None
        storage.schedule_meal.return_value = meal_id
        storage.get_meal_id_by_date_and_meal_type.return_value = meal_id
        storage.create_or_update_meal_items.return_value = None
        storage.create_meal.return_value = meal_id

        # act
        with pytest.raises(ItemNotFound):
            response = interactor.schedule_meal(schedule_meal_dto=schedule_meal_dto)

        # assert
        assert True

    def test_schedule_meal_with_invalid_item_quantity(self, storage):
        # arrange
        interactor = ScheduleMealInteractor(storage=storage)
        schedule_meal_dto = MagicMock()
        meal_id = "meal_id"
        storage.are_item_ids_valid.return_value = None
        storage.are_quantities_valid.return_value = True
        storage.schedule_meal.return_value = meal_id
        storage.get_meal_id_by_date_and_meal_type.return_value = meal_id
        storage.create_or_update_meal_items.return_value = None
        storage.create_meal.return_value = meal_id

        # act
        with pytest.raises(InvalidQuantity):
            response = interactor.schedule_meal(schedule_meal_dto=schedule_meal_dto)

        # assert
        assert True



