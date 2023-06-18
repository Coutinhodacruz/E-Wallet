from dtos.request.deposit_request import DepositRequest
from dtos.request.login_request import LoginRequest
from dtos.request.register_request import CreateAccountRequest
from dtos.request.transfer_request import TransferRequest
from dtos.request.withdraw_request import WithdrawRequest
from services.account_serviceImpl import AccountServiceImpl
from utils.account_not_found_exception import AccountNotFound
from utils.amount_can_not_be_greater_than_balance_exception import AmountCannotBeGreaterThanBalance
from utils.invalid_email import InvalidEmail
from utils.invalid_phone_number import InvalidPhoneNumber
from utils.negative_amount_exception import AmountCannotBeNegative
from utils.phone_number_exist_exception import PhoneNumberExist

account_service_impl = AccountServiceImpl()


class AccountController:

    @staticmethod
    def register(register_request: CreateAccountRequest) -> object:
        try:
            return account_service_impl.register_account(register_request)
        except (AccountNotFound, InvalidPhoneNumber, InvalidEmail, PhoneNumberExist) as exception:
            return str(exception)

    @staticmethod
    def login(login_request: LoginRequest) -> object:
        try:
            return account_service_impl.login(login_request)
        except (AccountNotFound, InvalidPhoneNumber) as exception:
            return str(exception)

    @staticmethod
    def deposit(deposit_request: DepositRequest) -> object:
        try:
            return account_service_impl.deposit_into(deposit_request)
        except (AccountNotFound, AmountCannotBeNegative) as exception:
            return str(exception)

    @staticmethod
    def check_balance(account_number: str) -> object:
        try:
            return account_service_impl.check_balance(account_number)
        except AccountNotFound as exception:
            return str(exception)

    @staticmethod
    def withdraw(withdraw_request: WithdrawRequest) -> object:
        try:
            return account_service_impl.withdraw_from(withdraw_request)
        except (AccountNotFound, AmountCannotBeNegative, AmountCannotBeGreaterThanBalance) as exception:
            return str(exception)

    @staticmethod
    def transfer(transfer_request: TransferRequest):
        try:
            return account_service_impl.transfer(transfer_request)
        except (AccountNotFound, AmountCannotBeNegative, AmountCannotBeGreaterThanBalance) as exception:
            return str(exception)
