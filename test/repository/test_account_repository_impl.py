from unittest import TestCase

from data.model.account import Account
from data.repository.account_repository_impl import AccountRepositoryImpl


class TestAccountRepositoryImpl(TestCase):

    def test_save_account(self):
        account_repository = AccountRepositoryImpl()
        account = Account()
        account.set_phone_number("09152652431")
        account_repository.add(account)
        print(account.get_account_number())
        self.assertEqual(1, account_repository.count())

    def test_two_account_can_be_saved(self):
        account_repository = AccountRepositoryImpl()
        bless_account = Account()
        sunday_account = Account()
        sunday_account.set_phone_number("08134132226")
        bless_account.set_phone_number("09152652431")

        account_repository.add(bless_account)
        account_repository.add(sunday_account)
        self.assertEqual(2, account_repository.count())

    def test_account_can_be_deleted(self):
        account_repository = AccountRepositoryImpl()
        bless_account = Account()
        bless_account.set_phone_number("09152652431")
        account_repository.add(bless_account)
        account_repository.delete("9152652431")
        self.assertEqual(0, account_repository.count())

    def test_one_account_can_be_deleted_after_adding_two(self):
        account_repository = AccountRepositoryImpl()
        bless_account = Account()
        sunday_account = Account()
        sunday_account.set_phone_number("08134132226")
        bless_account.set_phone_number("09152651431")
        account_repository.add(bless_account)
        account_repository.add(sunday_account)
        account_repository.delete("8134132226")
        self.assertEqual(1, account_repository.count())

    def test_find_by_account_number(self):
        account_repository = AccountRepositoryImpl()
        bless_account = Account()
        bless_account.set_phone_number("09152652431")
        account_repository.add(bless_account)
        self.assertEqual(bless_account, account_repository.find_by_account_number("9152652431"))
