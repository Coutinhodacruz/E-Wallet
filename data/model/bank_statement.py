import decimal


def print_bank_statement():
    print("=============================================================================")
    print("================================ BANK OF ZEN ================================")
    print("                         MONTHLY ACCOUNT STATEMENT ")
    print("Account Name: ")
    print("Account Number: ")
    print("Bank Balance: ")
    print("Date: ")
    print("=============================================================================")


class BankStatement:

    def __init__(self):
        self.__account_name: str = ""
        self.__account_number: str = ""
        self.__balance: decimal = 0.0
