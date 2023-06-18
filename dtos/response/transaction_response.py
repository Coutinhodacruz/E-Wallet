import decimal
from datetime import datetime
from typing import Type

from data.model.transaction_type import TransactionType


class TransactionResponse:
    def __init__(self):
        self.__amount: decimal = 0.00
        self.__transaction_type: TransactionType = TransactionType.DEBIT
        self.__account_name: str = ""
        self.__transaction_date_time = datetime.now().strftime("%Y-%m-%d %H-%M")

    def set_amount(self, amount: float):
        self.__amount = amount

    def get_amount(self) -> float:
        return self.__amount

    def set_transfer_type(self, transaction_type: TransactionType):
        self.__transaction_type = transaction_type

    def get_transaction_type(self, identity_number) -> TransactionType:
        return self.__transaction_type

    def set_account_name(self, account_name: str):
        self.__account_name = account_name

    def get_account_name(self) -> str:
        return self.__account_name

    def set_date_time(self, date_time: datetime):
        self.__transaction_date_time = date_time

    def __str__(self):
        return f"""Transaction Type: {self.__transaction_type.name}
Amount: {self.__amount}
Receiver's Name: {self.__account_name}
Date and Time: {datetime.now().strftime("%Y-%m-%d %H-%M")}"""
