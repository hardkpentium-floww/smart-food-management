import graphene

from meals.interactors.update_incampus_status_interactor import UpdateIncampusStatusInteractor
from meals.storages.storage_implementation import StorageImplementation
from meals_gql.user.types.types import UpdateIncampusStatusParams, UpdateIncampusStatusResponse, \
    IncampusStatusUpdateSuccess


class UpdateIncampusStatus(graphene.Mutation):
    class Arguments:
        params = UpdateIncampusStatusParams(required=True)

    Output = UpdateIncampusStatusResponse

    @staticmethod
    def mutate(root, info, params):
        storage = StorageImplementation()
        interactor = UpdateIncampusStatusInteractor(storage=storage)

        message = interactor.update_incampus_status(user_id=info.context.user_id, incampus_status=params.in_campus)


        return IncampusStatusUpdateSuccess(message=message)
