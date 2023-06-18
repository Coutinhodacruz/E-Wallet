import decimal


class TransferRequest:

    def __init__(self):
        self.__sender_account_number: str = ""
        self.__sender_account_name: str = ""
        self.__receiver_account_number: str = ""
        self.__receiver_account_name: str = ""
        self.__amount: decimal = 0.00
        self.__pin: str = ""

    def set_sender_account_number(self, sender_account_number: str):
        self.__sender_account_number = sender_account_number

    def get_sender_account_number(self) -> str:
        return self.__sender_account_number

    def set_sender_account_name(self, sender_account_name: str):
        self.__sender_account_name = sender_account_name

    def get_sender_account_name(self) -> str:
        return self.__sender_account_name

    def set_receiver_account_number(self, receiver_account_number: str):
        self.__receiver_account_number = receiver_account_number

    def get_receiver_account_number(self) -> str:
        return self.__receiver_account_number

    def set_receiver_account_name(self, receiver_account_name: str):
        self.__receiver_account_name = receiver_account_name

    def get_receiver_account_name(self) -> str:
        return self.__receiver_account_name

    def set_amount(self, amount: decimal):
        self.__amount = amount

    def get_amount(self) -> decimal:
        return self.__amount

    def set_pin(self, pin: str):
        self.__pin = pin

    def get_pin(self) -> str:
        return self.__pin
