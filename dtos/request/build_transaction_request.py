import decimal

from data.model.transaction_type import TransactionType


class BuildTransactionRequest:

    def __init__(self):
        self.__account_id: int = 0
        self.__amount: decimal = 0
        self.__account_name: str = ""
        self.__account_number: str = ""
        self.__transaction_type: TransactionType = TransactionType.NULL

    def set_account_id(self, account_id: int):
        self.__account_id = account_id

    def get_account_id(self) -> int:
        return self.__account_id

    def set_amount(self, amount: decimal):
        self.__amount = amount

    def get_amount(self) -> decimal:
        return self.__amount

    def set_account_name(self, account_name: str):
        self.__account_name = account_name

    def get_account_name(self) -> str:
        return self.__account_name

    def set_account_number(self, account_number: str):
        self.__account_number = account_number

    def get_account_number(self) -> str:
        return self.__account_number

    def set_transaction_type(self, transaction_type: TransactionType):
        self.__transaction_type = transaction_type

    def get_transaction_type(self) -> TransactionType:
        return self.__transaction_type
