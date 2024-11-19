import graphene

from graphql_service.custom_scalars import GQLDateTimeScalar


class TypeEnum(graphene.Enum):
    BREAKFAST = "BREAKFAST"
    LUNCH = "LUNCH"
    DINNER = "DINNER"

class FoodItemCategoryEnum(graphene.Enum):
    RICE = "RICE"
    PANCAKE = "PANCAKE"
    BEVERAGES = "BEVERAGES"

class BaseSizeUnitEnum(graphene.Enum):
    KG = "KG"
    PISCES = "PISCES"
    LITTERS = "LITTERS"

class ServingSizeUnitEnum(graphene.Enum):
    PISCES = "PISCES"
    LADDLE = "LADDLE"
    GLASS = "GLASS"


class MealTypeEnum(graphene.Enum):
    FULL= "FULL"
    HALF= "HALF"
    CUSTOM= "CUSTOM"


class Meal(graphene.ObjectType):
    id = graphene.String()
    date = graphene.DateTime()
    type = graphene.Field(TypeEnum)


class Item(graphene.ObjectType):
    id = graphene.String()
    name = graphene.String()
    category = graphene.Field(FoodItemCategoryEnum)
    base_size_unit = graphene.Field(BaseSizeUnitEnum)
    serving_size_unit = graphene.Field(ServingSizeUnitEnum)


class Items(graphene.ObjectType):
    items = graphene.List(Item)

class GetItemsParams(graphene.InputObjectType):
    offset = graphene.Int(required=True)
    limit = graphene.Int(required=True)

class ItemsNotFound(graphene.ObjectType):
    message = graphene.String()

class GetItemsResponse(graphene.Union):
    class Meta:
        types = (Items,ItemsNotFound)

class ScheduleMealParams(graphene.InputObjectType):
    item_ids = graphene.List(graphene.Int)
    full_meal_quantities = graphene.List(graphene.Int)
    half_meal_quantities = graphene.List(graphene.Int)
    date = GQLDateTimeScalar()
    type = graphene.Field(TypeEnum)
    meal_type = graphene.Field(MealTypeEnum)

class ScheduleMealSuccess(graphene.ObjectType):
    meal_id = graphene.String()

class ScheduleMealFailure(graphene.ObjectType):
    message = graphene.String()


class ScheduleMealResponse(graphene.Union):
    class Meta:
        types = (ScheduleMealSuccess, ScheduleMealFailure)

class AddItemsForUserParams(graphene.InputObjectType):
    user_id = graphene.String()
    item_ids = graphene.List(graphene.Int)
    quantities = graphene.List(graphene.Int)
    date = graphene.DateTime()
    type = graphene.Field(TypeEnum)
    meal_type = graphene.Field(MealTypeEnum)

class MealAddSuccess(graphene.ObjectType):
    user_meal_id = graphene.String()

class MealAddFailure(graphene.ObjectType):
    message = graphene.String()


class AddItemsForUserResponse(graphene.Union):
    class Meta:
        types = (MealAddSuccess, MealAddFailure)




