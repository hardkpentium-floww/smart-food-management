from debugpy.adapter import access_token
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from ...interactors.logout_interactor import LogoutInteractor
from ...storages.storage_implementation import StorageImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    user_id = str(kwargs['user'].user_id)
    access_token = kwargs['access_token']

    storage = StorageImplementation()
    interactor = LogoutInteractor(storage=storage)

    return interactor.logout(user_id=user_id, access_token=access_token)
