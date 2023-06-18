from dtos.request.complain_request import ComplainRequest
from dtos.response.complain_response import ComplainResponse


class ComplainService:

    def log_complain(self, complain_request: ComplainRequest) -> ComplainResponse:
        raise NotImplementedError

    def check_complain_status(self, identity_number: int) -> str:
        raise NotImplementedError
