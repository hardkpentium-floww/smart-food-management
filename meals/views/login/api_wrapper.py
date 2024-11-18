from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from ...interactors.login_interactor import LoginInteractor
from ...storages.storage_implementation import StorageImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    username = kwargs['request_data']['username']
    password = kwargs['request_data']['password']
    # user_id = kwargs['user'].id

    storage = StorageImplementation()
    interactor = LoginInteractor(storage=storage)

    return interactor.login(username=username,password=password)
