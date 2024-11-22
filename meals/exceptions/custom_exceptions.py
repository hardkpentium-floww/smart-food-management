from datetime import datetime
from typing import List

class ItemNotFound(Exception):
    def __init__(self, item_ids: List[str]):
        self.item_ids = item_ids

class InvalidQuantity(Exception):
    def __init__(self, quantities: List[int]):
        self.quantities = quantities

class InvalidDate(Exception):
    def __init__(self, date: datetime.date):
        self.date = date

class MealNotScheduledException(Exception):
    def __init__(self, date: datetime.date):
        self.date = date

class UserMealDoesNotExist(Exception):
    def __init__(self, user_id: str):
        self.user_id = user_id

class InvalidUser(Exception):
    def __init__(self, user_id: str):
        self.user_id = user_id

class InvalidMeal(Exception):
    def __init__(self, meal_id: str):
        self.meal_id = meal_id
