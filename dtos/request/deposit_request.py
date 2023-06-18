import decimal

from data.model.transaction_type import TransactionType


class DepositRequest:

    def __init__(self):
        self.__receivers_account_name: str = ""
        self.__receivers_account_number: str = ""
        self.__senders_account_name: str = ""
        self.__senders_account_number: str = ""
        # self.__account_name: str = ""
        self.__amount: decimal = 0.00
        self.__purpose: str = ""
        self.__transaction_type: TransactionType = TransactionType.CREDIT

    def set_receivers_account_name(self, account_name: str):
        self.__receivers_account_name = account_name

    def get_receivers_account_name(self) -> str:
        return self.__receivers_account_name

    def set_senders_name(self, account_name: str):
        self.__senders_account_name = account_name

    def get_senders_name(self) -> str:
        return self.__senders_account_name

    def set_senders_account_number(self, account_number: str):
        self.__senders_account_number = account_number

    def get_senders_account_number(self) -> str:
        return self.__senders_account_number

    def set_receivers_account_number(self, receivers_account_number: str):
        self.__receivers_account_number = receivers_account_number

    def get_receivers_account_number(self) -> str:
        return self.__receivers_account_number

    def set_amount(self, amount: decimal):
        self.__amount = amount

    def get_amount(self) -> decimal:
        return self.__amount

    def get_purpose(self) -> str:
        return self.__purpose

    def set_purpose(self, purpose: str):
        self.__purpose = purpose

    def get_transaction_type(self) -> TransactionType:
        return self.__transaction_type

    def set_transaction_type(self, transaction_type: TransactionType):
        self.__transaction_type = transaction_type
