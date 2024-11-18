import factory

from meals.constants.enums import MealTypeChoices, MealPreferenceTypeChoices, AteMealStatusChoices
from meals.interactors.storage_interfaces.storage_interface import AccessTokenDTO, RefreshTokenDTO, ScheduleMealDTO, \
    AddMealDTO, UserMealItemDTO
from meals.tests.factories.models import MealItemFactory


class AccessTokenDTOFactory(factory.Factory):
    class Meta:
        model = AccessTokenDTO

    user_id = factory.Faker("uuid4")
    token = factory.Faker("uuid4")
    application_id = factory.Faker("random_int", min=1, max=10000)
    expires = factory.Faker("date")
    scope = factory.Faker("name")



class RefreshTokenDTOFactory(factory.Factory):
    class Meta:
        model = RefreshTokenDTO

    user_id = factory.Faker("uuid4")
    refresh_token = factory.Faker("uuid4")
    application_id = factory.Faker("random_int", min=1, max=10000)
    access_token_id = factory.Faker("random_int", min=1, max=10000)


class ScheduleMealDTOFactory(factory.Factory):
    class Meta:
        model = ScheduleMealDTO

    item_ids = factory.List([factory.Faker("random_int", min=1, max=10000) for _ in range(10)])
    full_meal_quantities = factory.List([factory.Faker("random_int", min=1, max=10000) for _ in range(10)])
    half_meal_quantities = factory.List([factory.Faker("random_int", min=1, max=10000) for _ in range(10)])
    meal_type = factory.Iterator([choices[0] for choices in MealTypeChoices.get_list_of_tuples()])
    date = factory.Faker("date")

class MealItemDTOFactory(factory.Factory):
    class Meta:
        model = UserMealItemDTO

    item_id = factory.Faker("uuid4")
    quantity = factory.Faker("random_int", min=1, max=10000)




class AddMealDTOFactory(factory.Factory):
    class Meta:
        model = AddMealDTO

    user_id = factory.Faker("uuid4")
    meal_items: factory.SubFactory(MealItemDTOFactory)
    date = factory.Faker("date")
    meal_type = factory.Iterator([choice for choice in MealTypeChoices.get_list_of_values()])
    meal_preference=factory.Iterator([choice for choice in MealPreferenceTypeChoices.get_list_of_values()])
    meal_id= factory.Faker("uuid4")
    meal_status=factory.Iterator([choice for choice in AteMealStatusChoices.get_list_of_values()])