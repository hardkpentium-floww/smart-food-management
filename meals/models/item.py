from django.db import models
from ib_common.models import AbstractDateTimeModel

from meals.constants.enums import FoodItemCategoryChoices, BaseSizeUnitChoices, ServingSizeUnitChoices


class Item(AbstractDateTimeModel):
    id = models.CharField(primary_key=True, max_length=250)
    name = models.CharField(max_length=250)
    category = models.CharField(max_length=250, choices=FoodItemCategoryChoices.get_list_of_tuples(), default="RICE")
    base_size_unit = models.CharField(max_length=250, choices=BaseSizeUnitChoices.get_list_of_tuples() , default="KG")
    serving_size_unit = models.CharField(max_length=250, choices=ServingSizeUnitChoices.get_list_of_tuples(), default="LADDLE")


    def __str__(self):
        return self.name
