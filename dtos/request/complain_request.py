from xmlrpc.client import DateTime


class ComplainRequest:

    def __init__(self):
        self.__user_full_name: str = ""
        self.__user_email_address: str = ""
        self.__title_of_complain: str = ""
        self.__body_of_complain: str = ""
        self.__logged_date_of_complain = DateTime()

    def set_user_full_name(self, full_name: str):
        self.__user_full_name = full_name

    def get_user_full_name(self) -> str:
        return self.__user_full_name

    def set_user_email_address(self, email_address: str):
        self.__user_email_address = email_address

    def get_user_email_address(self) -> str:
        return self.__user_email_address

    def set_title_of_complain(self, title_of_complain: str):
        self.__title_of_complain = title_of_complain

    def get_title_of_complain(self) -> str:
        return self.__title_of_complain

    def set_body_of_complain(self, body_of_complain: str):
        self.__body_of_complain = body_of_complain

    def get_body_of_complain(self) -> str:
        return self.__body_of_complain

    def get_date_and_time(self) -> DateTime:
        return self.__logged_date_of_complain
