"""
# TODO: Update test case description
"""
import pytest
from django_swagger_utils.utils.test_utils import TestUtils
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX, URL_BASE_PATH
from ...factories.models import RefreshTokenFactory, UserFactory, ApplicationFactory, AccessTokenFactory, \
    UserAccountFactory


class TestCase01LogoutAPITestCase(TestUtils):
    APP_NAME = APP_NAME
    URL_BASE_PATH = URL_BASE_PATH
    OPERATION_NAME = OPERATION_NAME
    REQUEST_METHOD = REQUEST_METHOD
    URL_SUFFIX = URL_SUFFIX
    SECURITY = {'oauth': {'scopes': ['read']}}

    @pytest.mark.django_db
    def test_case(self, snapshot):
        user = UserFactory()
        application = ApplicationFactory(user_id=user.id)
        user_acc = UserAccountFactory(user_id=user.id)
        access_token = AccessTokenFactory(application_id=application.id, user_id=user.id)
        refresh_token = RefreshTokenFactory(user_id=user.id, application_id=application.id, access_token_id=access_token.id)

        body = {}
        path_params = {}
        query_params = {}
        headers = {
            "Authorization": f"Bearer {access_token.token}"
        }
        response = self.make_api_call(body=body,
                                      path_params=path_params,
                                      query_params=query_params,
                                      headers=headers,
                                      snapshot=snapshot)
