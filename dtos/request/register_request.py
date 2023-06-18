import decimal


class CreateAccountRequest:

    def __init__(self, ):
        self.__balance: decimal = 0.00
        self.__account_number: str = ""
        self.__first_name: str = ""
        self.__last_name: str = ""
        self.__phone_number: str = ""
        self.__pin: int = 0
        self.__password: str = ""
        self.__gmail: str = ""

    def get_balance(self) -> decimal:
        return self.__balance

    def get_first_name(self) -> str:
        return self.__first_name

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def get_last_name(self) -> str:
        return self.__last_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def get_phone_number(self) -> str:
        return self.__phone_number

    def set_phone_number(self, phone_number):
        self.__phone_number = phone_number

    def get_pin(self) -> int:
        return self.__pin

    def set_pin(self, pin: int):
        self.__pin = pin

    def get_account_number(self):
        return self.__account_number

    def set_account_number(self, account_number: str):
        self.__account_number = account_number

    def get_password(self):
        return self.__password

    def set_password(self, password: str):
        self.__password = password

    def set_gmail(self, gmail: str):
        self.__gmail = gmail

    def get_gmail(self) -> str:
        return self.__gmail
