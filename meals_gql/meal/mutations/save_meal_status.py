import graphene


from meals.exceptions.custom_exceptions import ItemNotFound, InvalidQuantity, InvalidDate
from meals.interactors.save_meal_status_interactor import SaveMealStatusInteractor
from meals.interactors.schedule_meal_interactor import ScheduleMealInteractor
from meals.interactors.storage_interfaces.storage_interface import ScheduleMealDTO
from meals.storages.storage_implementation import StorageImplementation
from meals_gql.meal.types.types import ScheduleMealParams, ScheduleMealResponse, ScheduleMealFailure, \
    ScheduleMealSuccess, SaveMealStatusParams, GetMealStatusResponse, MealStatus


class SaveMealStatus(graphene.Mutation):
    class Arguments:
        params = SaveMealStatusParams(required=True)

    Output = GetMealStatusResponse

    @staticmethod
    def mutate(root, info, params):
        storage = StorageImplementation()
        interactor = SaveMealStatusInteractor(storage=storage)

        meal_status = interactor.save_meal_status(meal_id=params.meal_id, meal_status=params.status, user_id=info.context.user_id)

        return MealStatus(meal_status=meal_status)
