import decimal

from data.model.transaction import Transaction
from utils.mail_sender import MailSender

mail_sender = MailSender()


class Account:

    def __init__(self):
        self.__id: int = 0
        self.__balance: decimal = 0.0
        self.__account_number: str = ""
        self.__first_name: str = ""
        self.__last_name: str = ""
        self.__phone_number: str = ""
        self.__pin: str = ""
        self.__password: str = ""
        self.__gmail: str = ""
        self.__transaction: list[Transaction] = []

    def __str__(self):
        return f"""
        Id: {self.__id}
        Full Name: {self.__first_name + " " + self.__last_name}
        Account Number: {self.__account_number}
        """

    def get_first_name(self) -> str:
        return self.__first_name

    def set_first_name(self, first_name: str):
        self.__first_name = first_name

    def get_last_name(self) -> str:
        return self.__last_name

    def set_last_name(self, last_name: str):
        self.__last_name = last_name

    def get_phone_number(self) -> str:
        return self.__phone_number

    def set_phone_number(self, phone_number: str):
        self.__phone_number = phone_number

    def get_pin(self) -> str:
        return self.__pin

    def set_pin(self, pin: str):
        self.__pin = pin

    def get_account_number(self) -> str:
        return self.__account_number

    def set_account_number(self, number: str):
        self.__account_number = number

    def set_password(self, password: str):
        self.__password = password

    def get_password(self):
        return self.__password

    def set_id(self, identity_number: int):
        self.__id = identity_number

    def get_id(self) -> int:
        return self.__id

    def get_balance(self):
        return self.__balance

    def set_transaction(self, transaction: list[Transaction]):
        self.__transaction = transaction

    def get_transaction(self):
        return self.__transaction

    def set_gmail(self, gmail: str):
        self.__gmail = gmail

    def get_gmail(self) -> str:
        return self.__gmail

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount
