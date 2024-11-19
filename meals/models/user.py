
from ib_common.models import AbstractDateTimeModel
from django.db import models


class User(AbstractDateTimeModel):
    id = models.CharField(primary_key=True, max_length=250)
    name = models.CharField(max_length=250)
    in_campus = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)


    def __str__(self):
        return self.name

