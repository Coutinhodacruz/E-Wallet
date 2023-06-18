import decimal
from datetime import datetime

from data.model.transaction_type import TransactionType


class Transaction:

    def __init__(self):
        self.__id: int = 0
        self.__account_id: int = 0
        self.__amount: decimal = 0.00
        self.__transaction_type: TransactionType = TransactionType.DEBIT
        self.__account_name: str = ""
        self.__transaction_date_time = datetime.now()

    def set_id(self, identity_number: int):
        self.__id = identity_number

    def get_id(self) -> int:
        return self.__id

    def set_account_id(self, identity_number: int):
        self.__account_id = identity_number

    def get_account_id(self) -> int:
        return self.__account_id

    def set_amount(self, amount: float):
        self.__amount = amount

    def get_amount(self) -> float:
        return self.__amount

    def set_transaction_type(self, transaction_type: TransactionType):
        self.__transaction_type = transaction_type

    def get_transaction_type(self) -> TransactionType:
        return self.__transaction_type

    def set_account_name(self, account_name: str):
        self.__account_name = account_name

    def get_account_name(self) -> str:
        return self.__account_name

    def get_date_time(self) -> datetime:
        return self.__transaction_date_time

    def __str__(self):
        return f"""   
            Id: {self.__id}
            Account Id: {self.__account_id}
            Amount: {self.__amount}
            Transaction Type: {self.__transaction_type.name}
            Account Name: {self.__account_name}
            Date and Time: {self.__transaction_date_time}"""
