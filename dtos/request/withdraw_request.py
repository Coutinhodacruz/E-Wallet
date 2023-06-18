import decimal
from datetime import datetime

from data.model.transaction_type import TransactionType


class WithdrawRequest:

    def __init__(self):
        self.__account_number: str = ""
        self.__amount: decimal = 0.00
        self.__receivers_account_name: str = ""
        self.__senders_account_name: str = ""
        self.__transaction_date_time = ""
        self.__transaction_type: TransactionType = TransactionType.DEBIT

    def __str__(self):
        return f"""
        Account Number: {self.__account_number}
        Amount: {self.__amount}
        Receiver Account Name: {self.__receivers_account_name}
        Senders Account Name: {self.__senders_account_name}
        Date & Time: {self.__transaction_date_time}
        Transaction Type: {self.__transaction_type}
        """

    def set_account_number(self, account_number: str):
        self.__account_number = account_number

    def get_account_number(self) -> str:
        return self.__account_number

    def set_amount(self, amount: decimal):
        self.__amount = amount

    def get_amount(self) -> decimal:
        return self.__amount

    def set_receivers_account_name(self, account_name: str):
        self.__receivers_account_name = account_name

    def get_receivers_account_name(self) -> str:
        return self.__receivers_account_name

    def set_senders_account_name(self, account_name: str):
        self.__senders_account_name = account_name

    def get_senders_account_name(self) -> decimal:
        return self.__senders_account_name

    def set_transaction_type(self, transaction_type: TransactionType):
        self.__transaction_date_time = transaction_type

    def get_transaction_type(self) -> TransactionType:
        return self.__transaction_type

    def get_transaction_date_time(self):
        self.__transaction_date_time = datetime.now().strftime("%Y-%m-%d %H:%M")
        return self.__transaction_date_time
