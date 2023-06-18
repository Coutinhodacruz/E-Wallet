import decimal

from dtos.request.deposit_request import DepositRequest
from dtos.request.login_request import LoginRequest
from dtos.request.register_request import CreateAccountRequest
from dtos.request.transfer_request import TransferRequest
from dtos.request.withdraw_request import WithdrawRequest
from dtos.response.deposit_response import DepositResponse
from dtos.response.login_response import LoginResponse
from dtos.response.register_response import RegisterResponse
from dtos.response.withdraw_response import WithdrawResponse


class AccountService:
    def register_account(self, request: CreateAccountRequest) -> RegisterResponse:
        raise NotImplementedError

    def login(self, login_request: LoginRequest) -> LoginResponse:
        raise NotImplementedError

    def deposit_into(self, deposit_request: DepositRequest) -> str:
        raise NotImplementedError

    def check_balance(self, account_number: str) -> decimal:
        raise NotImplementedError

    def withdraw_from(self, withdraw_request: WithdrawRequest) -> WithdrawResponse:
        raise NotImplementedError

    def transfer(self, transfer_request: TransferRequest):
        raise NotImplementedError
