from meals.exceptions.custom_exceptions import MealNotScheduledException
from meals.interactors.get_meal_status_interactory import GetMealStatusInteractor
from meals.interactors.get_scheduled_meal_by_admin_interactor import GetScheduledMealByAdminInteractor
from meals.storages.storage_implementation import StorageImplementation
from meals_gql.meal.types.types import MealNotScheduled, AdminScheduledMeal, MealStatus
from meals_gql.meal.types.types import MealItem

def resolve_get_meal_status(root, info, params):
    storage = StorageImplementation()
    interactor = GetMealStatusInteractor(storage=storage)

    meal_status = interactor.get_meal_status(meal_id=params.meal_id)


    return MealStatus(meal_status=meal_status)

