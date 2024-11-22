from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from ...interactors.login_interactor import LoginInteractor
from ...presenters.presenter_implementation import PresenterImplementation
from ...storages.storage_implementation import StorageImplementation


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    username = kwargs['request_data']['username']
    password = kwargs['request_data']['password']

    storage = StorageImplementation()
    interactor = LoginInteractor(storage=storage)
    presenter = PresenterImplementation()

    return interactor.login(username=username,password=password,presenter=presenter)
