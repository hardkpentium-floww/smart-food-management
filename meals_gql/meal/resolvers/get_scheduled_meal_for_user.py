from meals.exceptions.custom_exceptions import UserMealDoesNotExist
from meals.interactors.get_scheduled_meal_for_user_interactor import GetScheduledMealForUserInteractor
from meals.storages.storage_implementation import StorageImplementation
from meals_gql.meal.types.types import UserScheduledMeal, UserMeal, MealNotScheduled


def resolve_get_scheduled_meal_for_user(self, info,params):

    storage = StorageImplementation()
    interactor = GetScheduledMealForUserInteractor(storage=storage)

    try:
        response = interactor.get_scheduled_meal_for_user(user_id=info.context.user_id,date=params.date)
    except UserMealDoesNotExist:
        return MealNotScheduled(message="No Meal by User Scheduled")

    return response
