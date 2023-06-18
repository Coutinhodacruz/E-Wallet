from dtos.request.complain_request import ComplainRequest
from services.complain_service import ComplainService
from services.complain_service_impl import ComplainServiceImpl
from utils.account_not_found_exception import AccountNotFound
from utils.invalid_id import InvalidIdentityNumber

complain_service = ComplainServiceImpl()


class ComplainController:

    @staticmethod
    def log_complain(complain_request: ComplainRequest) -> object:
        try:
            return complain_service.log_complain(complain_request)
        except AccountNotFound as exception:
            return str(exception)

    @staticmethod
    def check_complaint_status(identity_number: int) -> object:
        try:
            return complain_service.check_complain_status(identity_number)
        except InvalidIdentityNumber as exception:
            return str(exception.__str__())
