from services.transaction_service_impl import TransactionServiceImpl

transaction_service = TransactionServiceImpl()


class TransactionController:

    @staticmethod
    def view_transaction(account_id: int) -> object:
        try:
            return transaction_service.find_transaction_by_account_id(account_id)
        except () as exception:
            return str(exception)
