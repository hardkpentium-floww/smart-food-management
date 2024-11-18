from django.http import JsonResponse

from meals.interactors.storage_interfaces.storage_interface import StorageInterface


class LoginInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def login(self, username:str, password: str):

        user = self.storage.get_user(username=username)



        if not user:
            invalid_username_response = {
                "status_code": 401,
                "res_status": "INVALID_USERNAME",
                "response": {
                    "message": "Invalid Username"
                }
            }
            return JsonResponse(data=invalid_username_response, status=401)

        user_acc = self.storage.get_user_acc(user_id=str(user.id))
        check_user_credentials = user_acc.check_password(password)

        if not check_user_credentials:
            invalid_credentials_response = {
                    "status_code": 401,
                    "res_status": "INVALID_PASSWORD",
                    "response": {
                        "message": "Invalid Password"
                    }
                }

            return JsonResponse(data=invalid_credentials_response, status=401)




        user_login_response = self.storage.login(user_id=user.id, username=username, password=password)

        login_response = {
              "status_code": 200,
              "res_status": "LOGIN_SUCCESS",
              "response": user_login_response
            }


        return JsonResponse(data=login_response, status=200)


