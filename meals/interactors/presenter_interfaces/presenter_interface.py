from abc import abstractmethod


class PresenterInterface:

    @abstractmethod
    def get_error_response_for_invalid_user(self):
        pass

    @abstractmethod
    def get_error_response_for_invalid_password(self):
        pass

    @abstractmethod
    def get_response_for_login(self,user_login_dto:any):
        pass

    @abstractmethod
    def get_response_for_logout(self):
        pass
