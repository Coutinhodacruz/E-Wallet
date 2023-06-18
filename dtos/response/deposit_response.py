import decimal


class DepositResponse:

    def __init__(self):
        self.__senders_name: str = ""
        self.__receiver_account_number: str = ""
        self.__receivers_name: str = ""
        self.__amount: decimal = 0.00

    def set_senders_name(self, senders_name: str):
        self.__senders_name = senders_name

    def get_senders_name(self) -> str:
        return self.__senders_name

    def set_receivers_name(self, receivers_name: str):
        self.__receivers_name = receivers_name

    def get_receivers_name(self) -> str:
        return self.__receivers_name

    def set_receiver_account(self, receiver_account: str):
        self.__receiver_account_number = receiver_account

    def get_receiver_account(self) -> str:
        return self.__receiver_account_number

    def set_amount(self, amount: decimal):
        self.__amount = amount

    def get_amount(self) -> decimal:
        return self.__amount

    def __str__(self):
        return f"""
            Senders Name: {self.__senders_name}
            Receivers Account: {self.__receiver_account_number}
            Receivers Name: {self.__receivers_name}
            Balance: {self.__amount}"""
