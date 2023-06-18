
from data.model.account import Account
from data.repository.account_repository import AccountRepository


class AccountRepositoryImpl(AccountRepository):
    def __init__(self):
        self.__accounts: list[Account] = []
        self.__counter = 0

    def delete(self, account_number: str) -> None:
        for account in self.__accounts:
            if account.get_account_number() == account_number:
                self.__accounts.remove(account)
                self.__counter -= 1
                break

    def add(self, account: Account) -> Account:
        if account.get_account_number() == "":
            account_number = self.generate_account_number(account.get_phone_number())
            account.set_account_number(account_number)

            if account.get_id() == 0:
                account_id = self.generate_account_id()
                account.set_id(account_id)
            self.__accounts.append(account)

        self.__counter += 1
        return account

    @staticmethod
    def generate_account_number(phone_number: str) -> str:
        phone_number = phone_number.lstrip("0")
        account_number = phone_number
        return account_number

    def count(self) -> int:
        return self.__counter

    def find_by_account_number(self, account_number: str) -> Account | None:
        for account in self.__accounts:
            if account.get_account_number() == account_number:
                return account
        return None

    def find_phone_number(self, phone_number) -> Account | None:
        for account in self.__accounts:
            if account.get_phone_number() == phone_number:
                return account
        return None

    def find_password(self, password):
        for account in self.__accounts:
            if account.get_password() == password:
                return account
        return None

    def generate_account_id(self):
        return self.__counter + 1
