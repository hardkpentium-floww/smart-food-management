from meals.constants.exception_messages import INVALID_USERNAME, INVALID_PASSWORD
from meals.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from meals.interactors.storage_interfaces.storage_interface import AccessTokenDTO


class PresenterImplementation(PresenterInterface):

    def get_error_response_for_invalid_user(self):
        status, response = INVALID_USERNAME
        data = {
            "status_code": 401,
            "res_status": status,
            "response": response
        }

    def get_error_response_for_invalid_password(self):
        status, response = INVALID_PASSWORD
        data = {
            "status_code": 401,
            "res_status": status,
            "response": response
        }

    def get_response_for_login(self, user_login_dto:UserLoginDTO):
        user_login_response = {
            "user_id": user_login_dto.user_id,
            "is_admin": user_login_dto.is_admin,
            "access_token": user_login_dto.access_token_str,
            "expires_in": user_login_dto.expires,
            "token_type": "Bearer",
            "scope": "read write",
            "refresh_token": user_login_dto.refresh_token_str
        }

        return user_login_response

    def get_response_for_logout(self):
        return {
            "response" : "logged out successfully"
        }

