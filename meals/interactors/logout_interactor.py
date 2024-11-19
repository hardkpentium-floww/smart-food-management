from django.http import JsonResponse

from meals.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from meals.interactors.storage_interfaces.storage_interface import StorageInterface
from meals.storages.storage_implementation import StorageImplementation


class LogoutInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def logout(self, access_token:str, user_id:str, presenter:PresenterInterface):
        access_token_id,refresh_token_id = self.storage.logout(user_id=user_id, access_token_str=access_token)
        self.storage.expire_access_token(access_token_id=access_token_id)
        self.storage.revoke_refresh_token(refresh_token_id=refresh_token_id)
        logout_response = presenter.get_response_for_logout()

        return JsonResponse(data=logout_response, status=200)


