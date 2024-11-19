from django.http import JsonResponse

from meals.interactors.presenter_interfaces.presenter_interface import PresenterInterface
from meals.interactors.storage_interfaces.storage_interface import StorageInterface
import uuid

class LoginInteractor:

    def __init__(self, storage: StorageInterface):
        self.storage = storage

    def login(self, username: str, password: str, presenter: PresenterInterface):
        from datetime import datetime, timedelta
        from meals.interactors.storage_interfaces.storage_interface import AccessTokenDTO, SessionTokensDTO

        user_id = self.storage.get_user_id(username=username)

        if not user_id:
            invalid_username_response = presenter.get_error_response_for_invalid_user()
            return JsonResponse(data=invalid_username_response, status=401)

        check_user_credentials = self.storage.is_password_valid(user_id=str(user_id), password=password)

        if not check_user_credentials:
            invalid_credentials_response = presenter.get_error_response_for_invalid_password()
            return JsonResponse(data=invalid_credentials_response, status=401)

        access_token_str = str(uuid.uuid4())
        refresh_token_str = str(uuid.uuid4())
        expires = datetime.now() + timedelta(days=1)
        application_id = self.storage.get_application_id(application_name="meals")
        is_admin = self.storage.check_admin(user_id=user_id)

        access_token_dto = AccessTokenDTO(
            user_id=user_id,
            token=access_token_str,
            application_id=application_id,
            expires=expires,
            scope="read write",
        )

        access_token_id = self.storage.create_access_token(access_token_dto=access_token_dto)

        refresh_token_dto = SessionTokensDTO(
            user_id=user_id,
            refresh_token=refresh_token_str,
            access_token_id=access_token_id,
            application_id=application_id
        )

        refresh_token_id = self.storage.create_refresh_token(refresh_token_dto=refresh_token_dto)

        user_login_dto = UserLoginDTO(
            user_id=user_id,
            is_admin=is_admin,
            access_token_str=access_token_str,
            expires=expires,
            refresh_token_str=refresh_token_str,
            token_type="Bearer",
            scope="read write"
        )

        login_response = presenter.get_response_for_login(user_login_dto=user_login_dto)
        return JsonResponse(data=login_response, status=200)
