from django.http import JsonResponse

from meals.interactors.storage_interfaces.storage_interface import StorageInterface
from meals.storages.storage_implementation import StorageImplementation


class LogoutInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def logout(self, access_token:str, user_id:str):

        self.storage.logout(user_id=user_id, access_token_str=access_token)

        logout_response = {
              "status_code": 200,
              "res_status": "LOGOUT SUCCESS",
              "response": {
                "message": "logged out successfully"
              }
            }

        return JsonResponse(data=logout_response, status=200)


