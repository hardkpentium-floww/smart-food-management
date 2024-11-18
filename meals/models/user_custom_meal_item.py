from django.db import models
from ib_common.models import AbstractDateTimeModel


class UserCustomMealItem(AbstractDateTimeModel):
    id = models.CharField(primary_key=True, max_length=250)
    item = models.ForeignKey('Item', on_delete=models.CASCADE, related_name="custom_meal_items")
    meal_qty = models.PositiveIntegerField(default=0)
    user_meal = models.ForeignKey('UserMeal', on_delete=models.CASCADE, related_name="user_custom_meal_items")

    def __str__(self):
        return self.item.name
