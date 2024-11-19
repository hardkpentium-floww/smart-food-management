from django.db import models
from ib_common.models import AbstractDateTimeModel

class MealItem(AbstractDateTimeModel):
    id = models.CharField(primary_key=True, max_length=250)
    meal = models.ForeignKey('Meal', on_delete=models.CASCADE, related_name="meal_items")
    item = models.ForeignKey('Item', on_delete=models.CASCADE, related_name="item_meal_items")
    full_meal_qty = models.PositiveIntegerField(default=0)
    half_meal_qty = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.item.name
