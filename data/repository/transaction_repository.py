from data.model.transaction import Transaction
from data.model.transaction_type import TransactionType


class TransactionRepository:
    def save(self, wallet: Transaction) -> Transaction:
        raise NotImplementedError

    def count(self) -> int:
        raise NotImplementedError

    def delete_transaction_by_id(self, identity_number: int):
        raise NotImplementedError

    def find_transaction_by_id(self, identity_number: int) -> list[Transaction]:
        raise NotImplementedError

    def find_transaction_by_account_id(self, account_id: int) -> list[Transaction]:
        raise NotImplementedError

    def find_all_credit_transaction(self, credit_type: TransactionType) -> list[Transaction]:
        raise NotImplementedError

    def find_all_debit_transaction(self, debit_type: TransactionType) -> list[Transaction]:
        raise NotImplementedError

    def view_all_transactions(self) -> list[Transaction]:
        raise NotImplementedError
