from django.db import models
from ib_common.models import AbstractDateTimeModel

from meals.constants.enums import MealTypeChoices, MealPreferenceTypeChoices, AteMealStatusChoices


class UserMeal(AbstractDateTimeModel):
    id = models.CharField(max_length=250, primary_key=True)
    user = models.ForeignKey('User', on_delete=models.CASCADE, related_name="user_meals")
    meal = models.ForeignKey('Meal', on_delete=models.CASCADE, related_name="user_meals")
    meal_type = models.CharField(max_length=250, choices=MealTypeChoices.get_list_of_tuples(), default="LUNCH")
    meal_preference = models.CharField(max_length=250, choices=MealPreferenceTypeChoices.get_list_of_tuples(), default="FULL")
    meal_status = models.CharField(max_length=250, choices=AteMealStatusChoices.get_list_of_tuples(), default="NULL")


    def __str__(self):
        return self.id
