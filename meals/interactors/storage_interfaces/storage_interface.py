from abc import abstractmethod
from datetime import datetime
from attr import dataclass
from ib_users.models import UserAccount
from typing import List

from meals.constants.enums import BaseSizeUnitType, FoodItemCategoryType, ServingSizeUnitType, MealType, \
    MealPreferenceType, AteMealStatusType
from meals_gql.meal.types.types import UserScheduledMeal


@dataclass
class AccessTokenDTO:
    access_token_id: str
    user_id: str
    token: str
    application_id: int
    expires: datetime
    scope: str

@dataclass
class SessionTokensDTO:
    refresh_token_id: int
    user_id: str
    refresh_token: str
    application_id: int
    access_token_id: str

@dataclass
class ItemDTO:
    item_id: str
    name: str
    category: FoodItemCategoryType
    base_size_unit: BaseSizeUnitType
    serving_size_unit: ServingSizeUnitType


@dataclass
class ScheduleMealDTO:
    item_ids: List[str]
    full_meal_quantities: List[int]
    half_meal_quantities: List[int]
    date: datetime
    meal_type: str

@dataclass
class MealItemDTO:
    meal_item_id: str
    name: str
    full_meal_qty: int
    half_meal_qty: int

@dataclass
class AdminScheduledMealDTO:
    date: datetime.date
    meal_type: str
    items: List[MealItemDTO]
    meal_id: str

@dataclass
class UserMealItemDTO:
    item_id: str
    quantity: int

@dataclass
class AddMealDTO:
    user_id: str
    meal_items: List[UserMealItemDTO]
    date: datetime
    meal_type: MealType
    meal_preference: MealPreferenceType
    meal_id: str
    meal_status: AteMealStatusType


class StorageInterface:

    @abstractmethod
    def logout(self, user_id:str, access_token_str:str):
        pass

    @abstractmethod
    def check_admin(self, user_id: str)->bool:
        pass

    @abstractmethod
    def is_password_valid(self, user_id:str, password:str)->bool:
        pass

    @abstractmethod
    def is_valid_user_id(self, user_id: str)->bool|str:
        pass

    @abstractmethod
    def is_valid_meal_id(self, meal_id: str)->bool|str:
        pass

    @abstractmethod
    def get_application_id(self, application_name: str)->int:
        pass

    @abstractmethod
    def expire_access_token(self, access_token_id:str)->None:
        pass

    @abstractmethod
    def revoke_refresh_token(self, refresh_token_id: str)->None:
        pass

    @abstractmethod
    def get_paginated_items(self, offset:int, limit:int)->List[ItemDTO]:
        pass

    @abstractmethod
    def get_user_acc(self, user_id: str)-> UserAccount:
        pass

    @abstractmethod
    def get_user_id(self, username:str)->str:
        pass

    @abstractmethod
    def create_access_token(self, access_token_dto:AccessTokenDTO)->str:
        pass


    @abstractmethod
    def create_meal(self,schedule_meal_dto:ScheduleMealDTO):
        pass


    @abstractmethod
    def get_meal_id_by_date_and_meal_type(self,date:datetime.date,meal_type:str):
        pass

    @abstractmethod
    def schedule_meal(self, schedule_meal_dto: ScheduleMealDTO)->str:
        pass

    @abstractmethod
    def create_or_update_meal_items(self, schedule_meal_dto:ScheduleMealDTO, meal_id:str):
        pass

    @abstractmethod
    def create_refresh_token(self, refresh_token_dto: SessionTokensDTO)->str:
        pass

    @abstractmethod
    def are_item_ids_valid(self, item_ids: [int]) -> List[str]:
        pass

    @abstractmethod
    def are_quantities_valid(self, quantities:[int]) -> List[int]:
        pass

    @abstractmethod
    def get_scheduled_meal_by_admin(self, meal_id:str,date:datetime.date, meal_type:str)->AdminScheduledMealDTO:
        pass

    @abstractmethod
    def get_meal_status(self, meal_id:str)->str:
        pass

    @abstractmethod
    def save_meal_status(self, meal_id:str, meal_status:str)->str:
        pass

    @abstractmethod
    def get_user_meal_preference(self, meal_id:str, user_id:str, meal_type:str)->str:
        pass

    @abstractmethod
    def create_user_meal(self, add_meal_dto: AddMealDTO)->str:
        pass

    @abstractmethod
    def add_custom_meal_items(self,user_meal_id:str, add_meal_dto: AddMealDTO)->str:
        pass

    @abstractmethod
    def update_incampus_status(self, user_id: str, incampus_status: bool)->str:
        pass


    @abstractmethod
    def get_scheduled_meal_for_user(self, user_id:str, date:datetime.date)->UserScheduledMeal:
        pass