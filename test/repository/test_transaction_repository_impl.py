from unittest import TestCase

from data.model.transaction import Transaction
from data.repository.transaction_repository_impl import TransactionRepositoryImpl


class TestTransaction_History_Impl(TestCase):

    def test_save_one_transaction_count_is_one(self):
        transaction = Transaction()
        transaction_history = TransactionRepositoryImpl()
        transaction_history.save(transaction)
        self.assertEqual(1, transaction_history.count())

    def test_save_two_transaction_count_is_two(self):
        transaction = Transaction()
        transaction_two = Transaction()
        transaction_history = TransactionRepositoryImpl()
        transaction_history.save(transaction)
        transaction_history.save(transaction_two)
        self.assertEqual(2, transaction_history.count())

    def test_delete_transaction_by_id(self):
        transaction = Transaction()
        transaction_two = Transaction()
        transaction_history = TransactionRepositoryImpl()
        transaction_history.save(transaction)
        self.assertEqual(1, transaction.get_id())
        transaction_history.save(transaction_two)
        self.assertEqual(2, transaction_two.get_id())
        transaction_history.delete_transaction_by_id(1)
        self.assertEqual(1, transaction_history.count())
