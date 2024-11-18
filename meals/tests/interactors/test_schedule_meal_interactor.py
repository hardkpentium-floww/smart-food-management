import json
from unittest.mock import create_autospec, patch, MagicMock
import pytest

from meals.exceptions.custom_exceptions import ItemNotFound, InvalidQuantity, InvalidDate, InvalidMealType
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
        meal_id = "meal_id"
        storage.validate_item_ids.return_value = True
        storage.validate_quantities.return_value = True
        storage.validate_date.return_value = True
        storage.check_meal_type.return_value = True
        storage.schedule_meal.return_value = meal_id

        # act
        response = interactor.schedule_meal(schedule_meal_dto=schedule_meal_dto)

        #assert
        assert response == meal_id

    def test_schedule_meal_with_invalid_item_id(self, storage):
        # arrange
        interactor = ScheduleMealInteractor(storage=storage)
        schedule_meal_dto = MagicMock()
        meal_id = "meal_id"
        storage.validate_item_ids.return_value = False
        storage.validate_quantities.return_value = True
        storage.validate_date.return_value = True
        storage.check_meal_type.return_value = True
        storage.schedule_meal.return_value = meal_id

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
        storage.validate_item_ids.return_value = True
        storage.validate_quantities.return_value = False
        storage.validate_date.return_value = True
        storage.check_meal_type.return_value = True
        storage.schedule_meal.return_value = meal_id

        # act
        with pytest.raises(InvalidQuantity):
            response = interactor.schedule_meal(schedule_meal_dto=schedule_meal_dto)

        # assert
        assert True

    def test_schedule_meal_with_invalid_meal_type(self, storage):
        # arrange
        interactor = ScheduleMealInteractor(storage=storage)
        schedule_meal_dto = MagicMock()
        meal_id = "meal_id"
        storage.validate_item_ids.return_value = True
        storage.validate_quantities.return_value = True
        storage.validate_date.return_value = True
        storage.check_meal_type.return_value = False
        storage.schedule_meal.return_value = meal_id

        # act
        with pytest.raises(InvalidMealType):
            response = interactor.schedule_meal(schedule_meal_dto=schedule_meal_dto)

        # assert
        assert True

    def test_schedule_meal_with_invalid_date(self, storage):
        # arrange
        interactor = ScheduleMealInteractor(storage=storage)
        schedule_meal_dto = MagicMock()
        meal_id = "meal_id"
        storage.validate_item_ids.return_value = True
        storage.validate_quantities.return_value = True
        storage.validate_date.return_value = False
        storage.check_meal_type.return_value = True
        storage.schedule_meal.return_value = meal_id

        # act
        with pytest.raises(InvalidDate):
            response = interactor.schedule_meal(schedule_meal_dto=schedule_meal_dto)

        # assert
        assert True

