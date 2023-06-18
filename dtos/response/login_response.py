import decimal


class LoginResponse:

    def __init__(self):
        self.__full_name: str = ""
        self.__email: str = ""
        self.__phone_number: str = ""
        self.__account_number: str = ""

    def set_full_name(self, full_name: str):
        self.__full_name = full_name

    def get_full_name(self) -> str:
        return self.__full_name

    def set_email(self, email: str):
        self.__email = email

    def get_email(self) -> str:
        return self.__email

    def set_phone_number(self, phone_number: str):
        self.__phone_number = phone_number

    def get_phone_number(self) -> str:
        return self.__phone_number

    def set_account_number(self, account_number: str):
        self.__account_number = account_number

    def get_account_balance(self) -> str:
        return self.__account_number

    def __str__(self):
        return f"""
        Account Number: {self.__account_number}
        Account Name: {self.__full_name}
        """
