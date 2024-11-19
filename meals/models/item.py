from django.db import models
from ib_common.models import AbstractDateTimeModel

from meals.constants.enums import FoodItemCategoryType, BaseSizeUnitType, ServingSizeUnitType


class Item(AbstractDateTimeModel):
    id = models.CharField(primary_key=True, max_length=250)
    name = models.CharField(max_length=250)
    category = models.CharField(max_length=250, choices=FoodItemCategoryType.get_list_of_tuples(), default=FoodItemCategoryType.get_list_of_values()[0][0])
    base_size_unit = models.CharField(max_length=250, choices=BaseSizeUnitType.get_list_of_tuples(), default=BaseSizeUnitType.get_list_of_values()[0])
    serving_size_unit = models.CharField(max_length=250, choices=ServingSizeUnitType.get_list_of_tuples(), default=ServingSizeUnitType.get_list_of_values()[0])


    def __str__(self):
        return self.name
