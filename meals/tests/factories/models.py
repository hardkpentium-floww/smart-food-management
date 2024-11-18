from datetime import datetime, timedelta

import factory
from ib_users.models import UserAccount
from oauth2_provider.models import Application, AccessToken, RefreshToken
from meals.models import UserMeal as UserMealModel, UserCustomMealItem
from meals.constants.enums import FoodItemCategoryChoices, BaseSizeUnitChoices, ServingSizeUnitChoices, MealTypeChoices, \
    MealPreferenceTypeChoices, AteMealStatusChoices
from meals.models import Item, Meal, MealItem

from meals.models.user import User
from meals_gql.meal.types.types import UserMeal


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    id = factory.Faker("uuid4")
    name = factory.Faker('name')
    in_campus = factory.Faker('boolean')


class UserAccountFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserAccount

    user_id = factory.Faker("uuid4")
    username = factory.Faker("name")

class ApplicationFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Application

    id = factory.Faker("random_int", min=1, max=10000)
    user_id = factory.Faker("uuid4")
    name = factory.Faker("name")


class AccessTokenFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = AccessToken

    user_id = factory.Faker("uuid4")
    token = factory.Faker("uuid4")
    application_id = factory.Faker("random_int", min=1,max=10000)
    expires = datetime.now() + timedelta(days=1)
    scope = factory.Faker("name")


class RefreshTokenFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = RefreshToken

    user_id = factory.Faker("uuid4")
    token = factory.Faker("uuid4")
    application_id = factory.Faker("random_int",min=1,max=10000)
    access_token_id = factory.Faker("random_int",min=1,max=10000)


class MealFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Meal

    id = factory.Faker("random_int", min=1, max=10000)
    date = factory.Faker("date")
    meal_type = factory.Iterator([choices[0] for choices in MealTypeChoices.get_list_of_tuples()])

class UserMealFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserMealModel

    id = factory.Faker("random_int", min=1, max=10000)
    user = factory.SubFactory(UserFactory)
    meal = factory.SubFactory(MealFactory)
    meal_type = factory.Iterator([choices[0] for choices in MealTypeChoices.get_list_of_tuples()])
    meal_preference = factory.Iterator([choices[0] for choices in MealPreferenceTypeChoices.get_list_of_tuples()])
    meal_status = factory.Iterator([choices[0] for choices in AteMealStatusChoices.get_list_of_tuples()])


class ItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Item

    id = factory.Faker("random_int", min=1, max=10000)
    name = factory.Faker("name")
    category = factory.Iterator([choice[0] for choice in FoodItemCategoryChoices.get_list_of_tuples()])
    base_size_unit = factory.Iterator([choice[0] for choice in BaseSizeUnitChoices.get_list_of_tuples()])
    serving_size_unit = factory.Iterator([choice[0] for choice in ServingSizeUnitChoices.get_list_of_tuples()])


class MealItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = MealItem

    id = factory.Faker("random_int", min=1, max=10000)
    meal = factory.SubFactory(MealFactory)
    item = factory.SubFactory(ItemFactory)
    full_meal_qty = factory.Faker("random_int", min=1, max=100)
    half_meal_qty = factory.Faker("random_int", min=1, max=100)


class UserCustomMealItemFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = UserCustomMealItem

    id = factory.Faker("uuid4")
    item = factory.SubFactory(ItemFactory)
    meal_qty = factory.Faker("random_int", min=1,max=1000)
    user_meal = factory.SubFactory(UserMealFactory)
