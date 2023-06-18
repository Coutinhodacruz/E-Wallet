from data.model.transaction import Transaction
from dtos.response.transaction_response import TransactionResponse


class TransactionService:

    def find_all_transaction(self) -> list[TransactionResponse]:
        raise NotImplementedError

    def find_transaction_by_account_id(self, identity_number: int) -> list[TransactionResponse]:
        raise NotImplementedError

    def view_all_debit_transaction(self) -> list[TransactionResponse]:
        raise NotImplementedError

    def view_all_credit_transaction(self) -> list[TransactionResponse]:
        raise NotImplementedError

    def print_bank_statement(self):
        raise NotImplementedError
