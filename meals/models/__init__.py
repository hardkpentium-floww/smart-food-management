from meals.models.item import Item
from meals.models.meal import Meal
from meals.models.user import User
from meals.models.user_meal import UserMeal
from meals.models.user_custom_meal_item import UserCustomMealItem
from meals.models.meal_item import MealItem

__all__ = [
    'Item',
    'Meal',
    'User',
    'UserMeal',
    'UserCustomMealItem',
    "MealItem"
]

# class DummyModel(AbstractDateTimeModel):
#     """
#     Model to store key value pair
#     Attributes:
#         :var key: String field which will be unique
#         :var value: String field which will be of 128 char length
#     """
#     key = models.CharField(max_length=128, unique=True)
#     value = models.CharField(max_length=128)
#
#     class Meta(object):
#         app_label = 'sample_app'
#
#     def __str__(self):
#         return "<DummyModel: {key}-{value}>".format(key=self.key,
#                                                     value=self.value)
#
