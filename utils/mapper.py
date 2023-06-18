from data.model.account import Account
from data.model.complain import Complain
from data.model.transaction import Transaction
from dtos.request.complain_request import ComplainRequest
from dtos.request.deposit_request import DepositRequest
from dtos.request.login_request import LoginRequest
from dtos.request.register_request import CreateAccountRequest
from dtos.response.complain_response import ComplainResponse
from dtos.response.deposit_response import DepositResponse
from dtos.response.login_response import LoginResponse
from dtos.response.register_response import RegisterResponse
from dtos.response.transaction_response import TransactionResponse


class Mapper:

    @staticmethod
    def map_request_with_account(request: CreateAccountRequest) -> Account:
        account = Account()
        account.set_gmail(request.get_gmail())
        account.set_last_name(request.get_last_name())
        account.set_first_name(request.get_first_name())
        account.set_phone_number(request.get_phone_number())
        account.set_password(request.get_password())
        return account

    @staticmethod
    def map_account_with_response(account: Account):
        response = RegisterResponse()
        response.set_account_number(account.get_account_number())
        response.set_gmail(account.get_gmail())
        response.set_full_name(account.get_first_name() + " " + account.get_last_name())
        response.set_balance(account.get_balance())
        return response

    @staticmethod
    def map_deposit_request_to_response(deposit_request: DepositRequest):
        response = DepositResponse()
        response.set_senders_name(deposit_request.get_senders_name())
        response.set_receiver_account(deposit_request.get_receivers_account_number())
        response.set_receivers_name(deposit_request.get_receivers_account_name())
        response.set_amount(deposit_request.get_amount())
        return response

    @staticmethod
    def map(login_request: LoginRequest):
        login_response = LoginResponse()
        login_response.set_full_name(login_request.get_full_name())
        login_response.set_account_number(login_request.get_account_number())
        return login_response

    @staticmethod
    def map_complain_request_with_complain(complain_request: ComplainRequest) -> Complain:
        complain = Complain()
        complain.set_user_full_name(complain_request.get_user_full_name())
        complain.set_user_email_address(complain_request.get_user_email_address())
        complain.set_title_of_complain(complain_request.get_title_of_complain())
        complain.set_body_of_complain(complain_request.get_body_of_complain())
        return complain

    @staticmethod
    def map_complain_with_complain_response(complain: Complain) -> ComplainResponse:
        complain_response = ComplainResponse()
        complain_response.set_id(complain.get_id())
        complain_response.set_user_full_name(complain.get_user_full_name())
        complain_response.set_title_of_complain(complain.get_title_of_complain())
        complain_response.set_user_email_address(complain.get_user_email_address())
        return complain_response

    @staticmethod
    def map_transaction_to_transaction_response(found_transaction: Transaction):
        transaction_response = TransactionResponse()
        transaction_response.set_amount(found_transaction.get_amount())
        transaction_response.set_transfer_type(found_transaction.get_transaction_type())
        transaction_response.set_account_name(found_transaction.get_account_name())
        transaction_response.set_date_time(found_transaction.get_date_time())
        return transaction_response
