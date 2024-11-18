
import graphene

from meals_gql.enums import FoodItemCategoryEnum, BaseSizeUnitEnum, ServingSizeUnitEnum


class Item(graphene.ObjectType):
    id = graphene.String()
    name = graphene.String()
    category = graphene.Field(FoodItemCategoryEnum)
    base_size_unit = graphene.Field(BaseSizeUnitEnum)
    serving_size_unit = graphene.Field(ServingSizeUnitEnum)


class Items(graphene.ObjectType):
    items = graphene.List(Item)

class GetItemsParams(graphene.InputObjectType):
    offset = graphene.Int()
    limit = graphene.Int()

class ItemsNotFound(graphene.ObjectType):
    message = graphene.String()

class GetItemsResponse(graphene.Union):
    class Meta:
        types = (Items,ItemsNotFound)
