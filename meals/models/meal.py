from django.db import models
from ib_common.models import AbstractDateTimeModel

from meals.constants.enums import MealTypeChoices


class Meal(AbstractDateTimeModel):
    id = models.CharField(max_length=250, primary_key=True)
    date = models.DateTimeField()
    meal_type = models.CharField(max_length=250, choices=MealTypeChoices.get_list_of_tuples(), default="LUNCH")



    def __str__(self):
        return self.id
