from meals.exceptions.custom_exceptions import MealNotScheduledException
from meals.interactors.get_scheduled_meal_by_admin_interactor import GetScheduledMealByAdminInteractor
from meals.storages.storage_implementation import StorageImplementation
from meals_gql.meal.types.types import MealNotScheduled, AdminScheduledMeal
from meals_gql.meal.types.types import MealItem

def resolve_get_scheduled_meal_by_admin(root, info, params):
    storage = StorageImplementation()
    interactor = GetScheduledMealByAdminInteractor(storage=storage)

    try:
        scheduled_meal_dto = interactor.get_scheduled_meal_by_admin(date=params.date, meal_type=params.meal_type.value)
    except MealNotScheduledException:
        return MealNotScheduled(message="No Meal Scheduled")

    item_dtos = scheduled_meal_dto.items

    items_type = [
        MealItem(
            id=item_dto.id,
            name=item_dto.name,
            full_meal_quantity=item_dto.full_meal_qty,
            half_meal_quantity=item_dto.half_meal_qty
        ) for item_dto in item_dtos
    ]

    return AdminScheduledMeal(
            date = scheduled_meal_dto.date,
            meal_type = scheduled_meal_dto.meal_type,
            items = items_type,
            meal_id = scheduled_meal_dto.meal_id
        )

