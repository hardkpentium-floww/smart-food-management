from sqlparse.utils import offset

from meals.exceptions.custom_exceptions import NoItemsFound
from meals.interactors.get_items_interactor import GetItemsInteractor
from meals.storages.storage_implementation import StorageImplementation
from meals_gql.item.types.types import Items, Item,ItemsNotFound


def resolve_get_items(root, info, params):
    storage = StorageImplementation()
    interactor = GetItemsInteractor(storage=storage)
    #
    try:
        item_dtos = interactor.get_items(offset=params.offset, limit=params.limit)
    except NoItemsFound:
        return ItemsNotFound(message="Items Not Found")

    return Items(items=[Item(
        id=item_dto.id,
        name=item_dto.name,
        category=item_dto.category,
        base_size_unit =item_dto.base_size_unit,
        serving_size_unit=item_dto.serving_size_unit
    ) for item_dto in item_dtos])
