from meals.interactors.get_meal_preference_interactor import GetMealPreferenceInteractor
from meals.storages.storage_implementation import StorageImplementation
from meals_gql.meal.types.types import UserMealPreference


def resolve_get_meal_preference(self, info,params):

    storage = StorageImplementation()
    interactor = GetMealPreferenceInteractor(storage=storage)

    meal_preference = interactor.get_meal_preference(user_id=params.user_id, meal_id=params.meal_id, meal_type=params.meal_type)

    return UserMealPreference(meal_preference=meal_preference)
    #
    # get_destinations_dto = GetDestinationsDTO(
    #     tag = params.tag,
    #     offset = params.offset,
    #     limit = params.limit
    # )
    #
    #
    # destination_dtos = interactor.get_destinations(get_destinations_dto=get_destinations_dto)
    #
    # return Destinations(destinations= [Destination(
    #         id=destination_dto.id,
    #         name=destination_dto.name,
    #         description=destination_dto.description,
    #         tags=destination_dto.tags,
    #         user_id=destination_dto.user_id
    #     )
    #     for destination_dto in destination_dtos])
    pass