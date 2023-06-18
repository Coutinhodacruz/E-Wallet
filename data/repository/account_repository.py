from data.model.account import Account


class AccountRepository:
    def add(self, account: Account) -> Account:
        raise NotImplementedError

    def count(self) -> int:
        raise NotImplementedError

    def delete(self, delete_by_id: int) -> None:
        raise NotImplementedError

    def find_by_account_number(self, account_number) -> Account:
        raise NotImplementedError

    def find_phone_number(self, phone_number) -> str:
        raise NotImplementedError
