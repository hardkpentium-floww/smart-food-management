from django.contrib import admin

from meals.models import UserMeal, UserCustomMealItem
from meals.models.meal_item import MealItem
from meals.models.meal import Meal
from meals.models.user import User
from meals.models.item import Item


admin.site.register(Item)
admin.site.register(Meal)
admin.site.register(MealItem)
admin.site.register(UserMeal)
admin.site.register(User)
admin.site.register(UserCustomMealItem)

