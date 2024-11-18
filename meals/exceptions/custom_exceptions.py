
class NoItemsFound(Exception):
    pass

class ItemNotFound(Exception):
    def __init__(self, item_id: str):
        self.item_id = item_id

class InvalidQuantity(Exception):
    pass

class InvalidDate(Exception):
    pass

class MealNotScheduledException(Exception):
    pass

class UserMealDoesNotExist(Exception):
    pass

class InvalidMealType(Exception):
    pass

class InvalidMealStatus(Exception):
    pass

class InvalidMealPreference(Exception):
    pass

class InvalidUser(Exception):
    pass

class InvalidMeal(Exception):
    pass

