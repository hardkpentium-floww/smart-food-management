import graphene

from meals.exceptions.custom_exceptions import InvalidUser, InvalidMeal, InvalidMealType, InvalidMealPreference, \
    InvalidMealStatus, ItemNotFound, InvalidQuantity
from meals.interactors.add_meal_for_user_interactor import AddMealForUserInteractor
from meals.interactors.storage_interfaces.storage_interface import AddMealDTO, UserMealItemDTO
from meals.storages.storage_implementation import StorageImplementation
from meals_gql.user.types.types import AddMealForUserParams, AddMealForUserResponse, MealAddSuccess, MealAddFailure


class AddMealForUser(graphene.Mutation):
    class Arguments:
        params = AddMealForUserParams(required=True)

    Output = AddMealForUserResponse

    @staticmethod
    def mutate(root, info, params):
        storage = StorageImplementation()
        interactor = AddMealForUserInteractor(storage=storage)

        meal_items = [
            UserMealItemDTO(
                item_id = item.item_id,
                quantity = item.quantity
            ) for item in params.meal_items
        ]

        add_meal_dto = AddMealDTO(
            user_id = info.context.user_id,
            meal_id = params.meal_id,
            meal_type = params.meal_type.value,
            meal_preference = params.meal_preference.value,
            date = params.date,
            meal_items= meal_items,
            meal_status=params.meal_status.value
        )

        try:
            user_meal_id = interactor.add_meal_for_user(add_meal_dto=add_meal_dto)
        except InvalidUser:
            return MealAddFailure(message= "Invalid User")
        except InvalidMeal:
            return MealAddFailure(message= "Invalid Meal ID")
        except InvalidMealType:
            return MealAddFailure(message= "Invalid Meal Type")
        except InvalidMealPreference:
            return MealAddFailure(message= "Invalid Meal Preference")
        except InvalidMealStatus:
            return MealAddFailure(message= "Invalid Meal Status")
        except ItemNotFound as e:
            return MealAddFailure(message= f"Invalid Item ID: {e.item_id}")
        except InvalidQuantity:
            return MealAddFailure(message= "Invalid Quantity")


        return MealAddSuccess(user_meal_id = user_meal_id)