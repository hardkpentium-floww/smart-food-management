import json
from unittest.mock import create_autospec, patch, Mock
import pytest

from meals.exceptions.custom_exceptions import InvalidUser, InvalidMeal, ItemNotFound, InvalidQuantity
from meals.interactors.add_meal_for_user_interactor import AddUserMealInteractor
from meals.interactors.storage_interfaces.storage_interface import StorageInterface


class TestInteractor:
    @pytest.fixture
    def storage(self):
        storage = create_autospec(StorageInterface)
        return storage


    def test_add_meal_for_user(self, storage):
        #arrange
        interactor = AddUserMealInteractor(storage=storage)
        add_meal_dto = Mock()
        add_meal_dto.meal_items = []
        user_meal_id = "user_meal_id"
        storage.is_valid_user_id.return_value = None
        storage.is_valid_meal_id.return_value = None
        storage.are_item_ids_valid.return_value= None
        storage.are_quantities_valid.return_value= None
        storage.create_user_meal.return_value = user_meal_id

        #act
        meal_id_res = interactor.add_meal_for_user(add_meal_dto=add_meal_dto)

        #assert
        assert meal_id_res == user_meal_id

    def test_add_meal_for_user_with_invalid_user(self, storage):
        # arrange
        interactor = AddUserMealInteractor(storage=storage)
        add_meal_dto = Mock()
        add_meal_dto.meal_items = []
        user_meal_id = "user_meal_id"
        storage.is_valid_user_id.return_value = True
        storage.is_valid_meal_id.return_value = None
        storage.are_item_ids_valid.return_value = None
        storage.are_quantities_valid.return_value = None
        storage.create_user_meal.return_value = user_meal_id

        # act
        with pytest.raises(InvalidUser):
            meal_id_res = interactor.add_meal_for_user(add_meal_dto=add_meal_dto)

        # assert
        assert True

    def test_add_meal_for_user_with_invalid_meal(self, storage):
        # arrange
        interactor = AddUserMealInteractor(storage=storage)
        add_meal_dto = Mock()
        add_meal_dto.meal_items = []
        user_meal_id = "user_meal_id"
        storage.is_valid_user_id.return_value = None
        storage.is_valid_meal_id.return_value = True
        storage.are_item_ids_valid.return_value = None
        storage.are_quantities_valid.return_value = None
        storage.create_user_meal.return_value = user_meal_id

        # act
        with pytest.raises(InvalidMeal):
            meal_id_res = interactor.add_meal_for_user(add_meal_dto=add_meal_dto)

        # assert
        assert True


    def test_add_meal_for_user_with_invalid_item_id(self, storage):
        # arrange
        interactor = AddUserMealInteractor(storage=storage)
        add_meal_dto = Mock()
        add_meal_dto.meal_items = []
        user_meal_id = "user_meal_id"
        storage.is_valid_user_id.return_value = None
        storage.is_valid_meal_id.return_value = None
        storage.are_item_ids_valid.return_value = True
        storage.are_quantities_valid.return_value = None
        storage.create_user_meal.return_value = user_meal_id

        # act
        with pytest.raises(ItemNotFound):
            meal_id_res = interactor.add_meal_for_user(add_meal_dto=add_meal_dto)

        # assert
        assert True

    def test_add_meal_for_user_with_invalid_item_quantity(self, storage):
        # arrange
        interactor = AddUserMealInteractor(storage=storage)
        add_meal_dto = Mock()
        add_meal_dto.meal_items = []
        user_meal_id = "user_meal_id"
        storage.is_valid_user_id.return_value = None
        storage.is_valid_meal_id.return_value = None
        storage.are_item_ids_valid.return_value = None
        storage.are_quantities_valid.return_value = True
        storage.create_user_meal.return_value = user_meal_id

        # act
        with pytest.raises(InvalidQuantity):
            meal_id_res = interactor.add_meal_for_user(add_meal_dto=add_meal_dto)

        # assert
        assert True
