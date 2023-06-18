import decimal


class LoginRequest:

    def __init__(self):
        self.__account_number: decimal = 0.00
        self.__password: str = ""
        self.__full_name: str = ""
        self.__account_id: int = 0

    def set_account_number(self, account_number: decimal):
        self.__account_number = account_number

    def get_account_number(self) -> decimal:
        return self.__account_number

    def set_account_id(self, account_id: int):
        self.__account_id = account_id

    def get_account_id(self) -> int:
        return self.__account_id

    def set_password(self, password: str):
        self.__password = password

    def get_password(self) -> str:
        return self.__password

    def set_full_name(self, fullname: str):
        self.__full_name = fullname

    def get_full_name(self) -> str:
        return self.__full_name
