import decimal
from typing import Any

from data.model.transaction import Transaction
from data.model.transaction_type import TransactionType
from data.repository.transaction_repository_impl import TransactionRepositoryImpl
from dtos.request.build_transaction_request import BuildTransactionRequest
from dtos.request.deposit_request import DepositRequest
from dtos.response.transaction_response import TransactionResponse
from services.transaction_service import TransactionService
from utils.mapper import Mapper
from typing import List


class TransactionServiceImpl(TransactionService):
    transaction_repository = TransactionRepositoryImpl()

    def find_transaction_by_account_id(self, account_id: int) -> str:
        found_transactions: List[Transaction] = self.transaction_repository.find_transaction_by_account_id(account_id)
        transaction_responses = []

        for transaction in found_transactions:
            transaction_response = Mapper.map_transaction_to_transaction_response(transaction)
            transaction_responses.append(str(transaction_response))

        return "\n\n".join(transaction_responses)

    def build_customer_transaction(self, build_transaction_request: BuildTransactionRequest):
        transaction = Transaction()
        transaction.set_amount(build_transaction_request.get_amount())
        transaction.set_account_name(build_transaction_request.get_account_name())
        transaction.set_transaction_type(build_transaction_request.get_transaction_type())
        transaction.set_account_id(build_transaction_request.get_account_id())
        self.transaction_repository.save(transaction)

    def view_all_debit_transaction(self) -> list[TransactionResponse]:
        pass

    def view_all_credit_transaction(self) -> list[TransactionResponse]:
        pass

    def print_bank_statement(self):
        pass

    def find_all_transaction(self) -> list[TransactionResponse]:
        pass
