from abc import abstractmethod
from datetime import datetime
from attr import dataclass


@dataclass
class AccessTokenDTO:
    user_id: str
    token: str
    application_id: int
    expires: datetime
    scope: str

@dataclass
class RefreshTokenDTO:
    user_id: str
    refresh_token: str
    application_id: int
    access_token_id: str

@dataclass
class ItemDTO:
    id: str
    name: str
    category: str
    base_size_unit: str
    serving_size_unit: str


@dataclass
class ScheduleMealDTO:
    item_ids: [str]
    full_meal_quantities: [int]
    half_meal_quantities: [int]
    date: datetime
    meal_type: str

@dataclass
class MealItemDTO:
    id: str
    name: str
    full_meal_qty: int
    half_meal_qty: int

@dataclass
class AdminScheduledMealDTO:
    date: datetime
    meal_type: str
    items: [MealItemDTO]
    meal_id: str

@dataclass
class UserMealItemDTO:
    item_id: str
    quantity: int

@dataclass
class AddMealDTO:
    user_id: str
    meal_items: [UserMealItemDTO]
    date: datetime
    meal_type: str
    meal_preference: str
    meal_id: str
    meal_status: str


class StorageInterface:
    @abstractmethod
    def login(self, username: str, user_id: str, password:str):
        pass

    @abstractmethod
    def logout(self, user_id:str, access_token_str:str):
        pass

    @abstractmethod
    def check_admin(self, user_id: str):
        pass

    @abstractmethod
    def validate_user(self, user_id: str):
        pass

    @abstractmethod
    def validate_meal(self, meal_id: str):
        pass

    @abstractmethod
    def get_application_id(self, application_name: str):
        pass


    @abstractmethod
    def expire_access_token(self, access_token_id:str):
        pass

    @abstractmethod
    def revoke_refresh_token(self, refresh_token_id: str):
        pass

    @abstractmethod
    def get_items(self,offset:int,limit:int):
        pass

    @abstractmethod
    def get_user_acc(self, user_id: str):
        pass

    @abstractmethod
    def get_user(self, username:str):
        pass

    @abstractmethod
    def create_access_token(self, access_token_dto:AccessTokenDTO):
        pass

    @abstractmethod
    def schedule_meal(self, schedule_meal_dto: ScheduleMealDTO):
        pass

    @abstractmethod
    def create_refresh_token(self, refresh_token_dto: RefreshTokenDTO):
        pass

    @abstractmethod
    def validate_item_ids(self, item_ids: [int]):
        pass

    @abstractmethod
    def validate_quantities(self, quantities:[int]):
        pass

    @abstractmethod
    def validate_date(self, date: datetime):
        pass

    @abstractmethod
    def get_scheduled_meal_by_admin(self, date: datetime, meal_type:str):
        pass

    @abstractmethod
    def get_meal_status(self, meal_id:str):
        pass

    @abstractmethod
    def save_meal_status(self, meal_id:str, meal_status:str):
        pass

    @abstractmethod
    def get_meal_preference(self, meal_id:str, user_id:str, meal_type:str):
        pass

    @abstractmethod
    def check_meal_type(self, meal_type:str):
        pass

    @abstractmethod
    def check_meal_status(self, meal_status:str):
        pass

    @abstractmethod
    def check_meal_preference(self, meal_preference:str):
        pass

    @abstractmethod
    def add_meal_for_user(self, add_meal_dto: AddMealDTO):
        pass

    @abstractmethod
    def update_incampus_status(self, user_id: str, incampus_status: bool):
        pass


    @abstractmethod
    def get_scheduled_meal_for_user(self, user_id:str, date:datetime):
        pass