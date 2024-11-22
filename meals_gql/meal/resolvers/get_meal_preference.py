from meals.exceptions.custom_exceptions import InvalidMeal
from meals.interactors.get_meal_preference_interactor import GetMealPreferenceInteractor
from meals.storages.storage_implementation import StorageImplementation
from meals_gql.meal.types.types import UserMealPreference, MealNotScheduled


def resolve_get_user_meal_preference(self, info, params):

    storage = StorageImplementation()
    interactor = GetMealPreferenceInteractor(storage=storage)

    try:
        meal_preference = interactor.get_user_meal_preference(user_id=info.context.user_id, meal_id=params.meal_id, meal_type=params.meal_type)
    except InvalidMeal as e:
        return MealNotScheduled(message=f'Invalid Meal ID {e.meal_id}')

    return UserMealPreference(meal_preference=meal_preference)
