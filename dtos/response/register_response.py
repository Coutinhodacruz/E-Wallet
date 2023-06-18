import decimal


class RegisterResponse:
    def __init__(self):
        self.__balance: decimal = 0.00
        self.__account_number: str = ""
        self.__full_name: str = ""
        self.__gmail: str = ""

    def get_account_number(self):
        return self.__account_number

    def set_account_number(self, account_number):
        self.__account_number = account_number

    def get_full_name(self):
        return self.__full_name

    def set_full_name(self, full_name):
        self.__full_name = full_name

    def get_gmail(self):
        return self.__gmail

    def set_gmail(self, gmail):
        self.__gmail = gmail

    def set_balance(self, param):
        self.__balance = param

    def __str__(self):
        return f"""
         Account Number: {self.__account_number}
         Email: {self.__gmail}
         Full Name: {self.__full_name}
         Balance: {self.__balance}"""
