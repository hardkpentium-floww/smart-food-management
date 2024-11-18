import json
from unittest.mock import create_autospec, patch, Mock
import pytest

from meals.exceptions.custom_exceptions import InvalidUser, InvalidMealType, InvalidMeal, InvalidMealStatus, \
    InvalidMealPreference, ItemNotFound, InvalidQuantity
from meals.interactors.add_meal_for_user_interactor import AddMealForUserInteractor
from meals.interactors.login_interactor import LoginInteractor
from meals.interactors.logout_interactor import LogoutInteractor
from meals.interactors.storage_interfaces.storage_interface import StorageInterface
from meals.tests.factories.models import UserAccountFactory, UserFactory


class TestInteractor:
    @pytest.fixture
    def storage(self):
        storage = create_autospec(StorageInterface)
        return storage


    def test_add_meal_for_user(self, storage):
        #arrange
        interactor = AddMealForUserInteractor(storage=storage)
        add_meal_dto = Mock()
        add_meal_dto.meal_items = []
        user_meal_id = "user_meal_id"
        storage.validate_user.return_value = True
        storage.validate_meal.return_value = True
        storage.check_meal_type.return_value= True
        storage.check_meal_status.return_value= True
        storage.check_meal_preference.return_value= True
        storage.validate_item_ids.return_value= True
        storage.validate_quantities.return_value= True
        storage.add_meal_for_user.return_value = user_meal_id

        #act
        meal_id_res = interactor.add_meal_for_user(add_meal_dto=add_meal_dto)

        #assert
        assert meal_id_res == user_meal_id

    def test_add_meal_for_user_with_invalid_user(self, storage):
        # arrange
        interactor = AddMealForUserInteractor(storage=storage)
        add_meal_dto = Mock()
        add_meal_dto.meal_items = []
        user_meal_id = "user_meal_id"
        storage.validate_user.return_value = False
        storage.validate_meal.return_value = True
        storage.check_meal_type.return_value = True
        storage.check_meal_status.return_value = True
        storage.check_meal_preference.return_value = True
        storage.validate_item_ids.return_value = True
        storage.validate_quantities.return_value = True
        storage.add_meal_for_user.return_value = user_meal_id

        # act
        with pytest.raises(InvalidUser):
            meal_id_res = interactor.add_meal_for_user(add_meal_dto=add_meal_dto)

        # assert
        assert True

    def test_add_meal_for_user_with_invalid_meal(self, storage):
        # arrange
        interactor = AddMealForUserInteractor(storage=storage)
        add_meal_dto = Mock()
        add_meal_dto.meal_items = []
        user_meal_id = "user_meal_id"
        storage.validate_user.return_value = True
        storage.validate_meal.return_value = False
        storage.check_meal_type.return_value = True
        storage.check_meal_status.return_value = True
        storage.check_meal_preference.return_value = True
        storage.validate_item_ids.return_value = True
        storage.validate_quantities.return_value = True
        storage.add_meal_for_user.return_value = user_meal_id

        # act
        with pytest.raises(InvalidMeal):
            meal_id_res = interactor.add_meal_for_user(add_meal_dto=add_meal_dto)

        # assert
        assert True

    def test_add_meal_for_user_with_invalid_meal_type(self, storage):
        # arrange
        interactor = AddMealForUserInteractor(storage=storage)
        add_meal_dto = Mock()
        add_meal_dto.meal_items = []
        user_meal_id = "user_meal_id"
        storage.validate_user.return_value = True
        storage.validate_meal.return_value = True
        storage.check_meal_type.return_value = False
        storage.check_meal_status.return_value = True
        storage.check_meal_preference.return_value = True
        storage.validate_item_ids.return_value = True
        storage.validate_quantities.return_value = True
        storage.add_meal_for_user.return_value = user_meal_id

        # act
        with pytest.raises(InvalidMealType):
            meal_id_res = interactor.add_meal_for_user(add_meal_dto=add_meal_dto)

        # assert
        assert True

    def test_add_meal_for_user_with_invalid_meal_status(self, storage):
        # arrange
        interactor = AddMealForUserInteractor(storage=storage)
        add_meal_dto = Mock()
        add_meal_dto.meal_items = []
        user_meal_id = "user_meal_id"
        storage.validate_user.return_value = True
        storage.validate_meal.return_value = True
        storage.check_meal_type.return_value = True
        storage.check_meal_status.return_value = False
        storage.check_meal_preference.return_value = True
        storage.validate_item_ids.return_value = True
        storage.validate_quantities.return_value = True
        storage.add_meal_for_user.return_value = user_meal_id

        # act
        with pytest.raises(InvalidMealStatus):
            meal_id_res = interactor.add_meal_for_user(add_meal_dto=add_meal_dto)

        # assert
        assert True

    def test_add_meal_for_user_with_invalid_meal_preference(self, storage):
        # arrange
        interactor = AddMealForUserInteractor(storage=storage)
        add_meal_dto = Mock()
        add_meal_dto.meal_items = []
        user_meal_id = "user_meal_id"
        storage.validate_user.return_value = True
        storage.validate_meal.return_value = True
        storage.check_meal_type.return_value = True
        storage.check_meal_status.return_value = True
        storage.check_meal_preference.return_value = False
        storage.validate_item_ids.return_value = True
        storage.validate_quantities.return_value = True
        storage.add_meal_for_user.return_value = user_meal_id

        # act
        with pytest.raises(InvalidMealPreference):
            meal_id_res = interactor.add_meal_for_user(add_meal_dto=add_meal_dto)

        # assert
        assert True

    def test_add_meal_for_user_with_invalid_item_id(self, storage):
        # arrange
        interactor = AddMealForUserInteractor(storage=storage)
        add_meal_dto = Mock()
        add_meal_dto.meal_items = []
        user_meal_id = "user_meal_id"
        storage.validate_user.return_value = True
        storage.validate_meal.return_value = True
        storage.check_meal_type.return_value = True
        storage.check_meal_status.return_value = True
        storage.check_meal_preference.return_value = True
        storage.validate_item_ids.return_value = False
        storage.validate_quantities.return_value = True
        storage.add_meal_for_user.return_value = user_meal_id

        # act
        with pytest.raises(ItemNotFound):
            meal_id_res = interactor.add_meal_for_user(add_meal_dto=add_meal_dto)

        # assert
        assert True

    def test_add_meal_for_user_with_invalid_item_quantity(self, storage):
        # arrange
        interactor = AddMealForUserInteractor(storage=storage)
        add_meal_dto = Mock()
        add_meal_dto.meal_items = []
        user_meal_id = "user_meal_id"
        storage.validate_user.return_value = True
        storage.validate_meal.return_value = True
        storage.check_meal_type.return_value = True
        storage.check_meal_status.return_value = True
        storage.check_meal_preference.return_value = True
        storage.validate_item_ids.return_value = True
        storage.validate_quantities.return_value = False
        storage.add_meal_for_user.return_value = user_meal_id

        # act
        with pytest.raises(InvalidQuantity):
            meal_id_res = interactor.add_meal_for_user(add_meal_dto=add_meal_dto)

        # assert
        assert True
