from unittest import TestCase

from utils.mail_sender import MailSender
from dtos.request.deposit_request import DepositRequest
from dtos.request.login_request import LoginRequest
from dtos.request.register_request import CreateAccountRequest
from dtos.request.transfer_request import TransferRequest
from dtos.request.withdraw_request import WithdrawRequest
from services.account_serviceImpl import AccountServiceImpl
from utils.negative_amount_exception import AmountCannotBeNegative
from utils.phone_number_exist_exception import PhoneNumberExist


class TestAccountServiceImpl(TestCase):

    def test_account_can_be_registered(self):
        account_service = AccountServiceImpl()
        request = CreateAccountRequest()
        mail_sender = MailSender()

        request.set_first_name("sunday")
        request.set_last_name("emmanuel")
        request.set_gmail("sunday-emmanuel@gmail.com")
        request.set_phone_number("08023677114")
        request.set_password("pass")
        request.set_account_number(request.get_account_number())

        mail_sender.email_alert("Account Registration", """
        Congratulations!
        You have successfully created
        an account with instant pay e_wallet
        """, request.get_gmail())
        expected = """
         Account Number: 8023677114
         Email: sunday-emmanuel@gmail.com
         Full Name: sunday emmanuel
         Balance: 0.0"""
        self.assertEqual(expected, account_service.register_account(request).__str__())

    def test_register_with_same_phone_number_throw_exception(self):
        account_service = AccountServiceImpl()
        register_request = CreateAccountRequest()

        register_request.set_phone_number("09045788992")
        register_request.set_password("4444")
        register_request.set_gmail("t@gmail.com")
        account_service.register_account(register_request)

        register_request.set_phone_number("09045765992")
        register_request.set_password("5555")
        register_request.set_gmail("same@gmail.com")
        account_service.register_account(register_request)
        with self.assertRaises(PhoneNumberExist):
            account_service.register_account(register_request)

    def test_user_can_login_in(self):
        request = CreateAccountRequest()
        request.set_phone_number("08198765432")
        request.set_password("pass")
        request.set_first_name("Austin")
        request.set_last_name("Barbel")
        request.set_gmail("austin-barbel@gmail.com")

        account_service = AccountServiceImpl()
        account_service.register_account(request)

        login_request = LoginRequest()
        login_request.set_account_number("8198765432")
        login_request.set_password("pass")
        self.assertTrue(account_service.login(login_request))

    def test_send_money_from_account_one_to_account_two(self):
        account_service = AccountServiceImpl()

        request = CreateAccountRequest()
        request.set_phone_number("09153752431")
        request.set_password("1234")
        request.set_first_name("Sunday")
        request.set_last_name("Emma")
        request.set_gmail("emma-sunday@gmail.com")
        account_service.register_account(request)

        deposit_request = DepositRequest()
        deposit_request.set_receivers_account_number("9153752431")
        deposit_request.set_receivers_account_name("Sunday Emma")
        deposit_request.set_amount(4000.0)
        self.assertEqual("Sent Successfully", account_service.deposit_into(deposit_request))

        request_two = CreateAccountRequest()
        request_two.set_phone_number("07023677114")
        request_two.set_password("5678")
        request_two.set_first_name("Zainab")
        request_two.set_last_name("Alice")
        request_two.set_gmail("zainab@gmail.com")
        account_service.register_account(request_two)
        self.assertEqual(0.0, account_service.check_balance("7023677114"))

        transfer_request = TransferRequest()
        transfer_request.set_sender_account_number("9153752431")
        transfer_request.set_sender_account_name("Sunday Emma")
        transfer_request.set_receiver_account_number("7023677114")
        transfer_request.set_receiver_account_name("Zainab Alice")
        transfer_request.set_amount(3000)
        transfer_request.set_pin("1234")

        account_service.transfer(transfer_request)

        self.assertEqual(1000.0, account_service.check_balance("9153752431"))
        self.assertEqual(3000.0, account_service.check_balance("7023677114"))

    def test_money_can_be_deposited(self):
        request = CreateAccountRequest()
        request.set_phone_number("09152652431")
        request.set_password("1234")
        request.set_first_name("Sunday")
        request.set_last_name("Emma")
        request.set_gmail("emma-sunday@gmail.com")

        account_service = AccountServiceImpl()
        account_service.register_account(request)

        deposit_request = DepositRequest()
        deposit_request.set_receivers_account_number("9152652431")
        deposit_request.set_receivers_account_name(request.get_first_name() + " " + request.get_last_name())
        deposit_request.set_amount(4000.0)
        account_service.deposit_into(deposit_request)

        deposit_request.set_amount(4000.0)
        account_service.deposit_into(deposit_request)
        self.assertEqual(8000.0, account_service.check_balance("9152652431"))

        expected = "Sent Successfully"
        self.assertEqual(expected, account_service.deposit_into(deposit_request).__str__())

    def test_deposit_negative_amount_throw_exception(self):
        request = CreateAccountRequest()
        request.set_phone_number("08123455667")
        request.set_password("7865")
        request.set_gmail("request@gmail.com")
        request.set_first_name("sunday")
        request.set_last_name("emma")

        account_service = AccountServiceImpl()
        account_service.register_account(request)

        deposit_request = DepositRequest()
        deposit_request.set_receivers_account_number("8123455667")
        deposit_request.set_amount(100.0)
        account_service.deposit_into(deposit_request)
        self.assertEqual(100.0, account_service.check_balance("8123455667"))

        try:
            deposit_request.set_amount(-30000.0)
            account_service.deposit_into(deposit_request)
            with self.assertRaises(AmountCannotBeNegative):
                account_service.deposit_into(deposit_request)
        except AmountCannotBeNegative:
            print("Amount can not be negative")

    def test_money_can_be_withdrawn(self):
        request = CreateAccountRequest()
        request.set_phone_number("08030669508")
        request.set_password("9999")
        request.set_first_name("Sunday")
        request.set_last_name("Emma")
        request.set_gmail("sunday-email@gmail.com")

        account_service = AccountServiceImpl()
        account_service.register_account(request)

        deposit_request = DepositRequest()
        deposit_request.set_receivers_account_number("8030669508")
        deposit_request.set_amount(5000.00)

        account_service.deposit_into(deposit_request)

        withdraw_request = WithdrawRequest()
        withdraw_request.set_account_number("8030669508")
        withdraw_request.set_amount(1000.0)

        account_service.withdraw_from(withdraw_request)
        self.assertEqual(4000.0, account_service.check_balance("8030669508"))
