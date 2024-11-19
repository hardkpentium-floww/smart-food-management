from django.db import models
from ib_common.models import AbstractDateTimeModel
from meals.constants.enums import MealType


class Meal(AbstractDateTimeModel):
    id = models.CharField(max_length=250, primary_key=True)
    date = models.DateField()
    meal_type = models.CharField(max_length=250, choices=MealType.get_list_of_tuples(), default=MealType.get_list_of_values()[0])

    def __str__(self):
        return self.id
