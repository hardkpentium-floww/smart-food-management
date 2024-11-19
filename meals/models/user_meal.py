from django.db import models
from ib_common.models import AbstractDateTimeModel

from meals.constants.enums import *


class UserMeal(AbstractDateTimeModel):
    id = models.CharField(max_length=250, primary_key=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name="user_meals")
    meal = models.ForeignKey('Meal', on_delete=models.CASCADE, related_name="user_meals")
    meal_type = models.CharField(max_length=250, choices=MealType.get_list_of_tuples(), default=MealType.get_list_of_values()[0])
    meal_preference = models.CharField(max_length=250, choices=MealPreferenceType.get_list_of_tuples(), default=MealPreferenceType.get_list_of_values()[0])
    meal_status = models.CharField(max_length=250, choices=AteMealStatusType.get_list_of_tuples(), default=AteMealStatusType.get_list_of_values()[0])

    def __str__(self):
        return self.id
