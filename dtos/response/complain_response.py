from xmlrpc.client import DateTime

from data.model.complain_type import ComplainType


class ComplainResponse:

    def __init__(self):
        self.__id: str = ""
        self.__user_full_name: str = ""
        self.__user_email_address: str = ""
        self.__title_of_complain: str = ""
        self.__status_of_user_complaint = ComplainType.UNASSIGNED.name
        self.__logged_date_of_complain = DateTime()

    def set_id(self, identity_number: str):
        self.__id = identity_number

    def get_id(self) -> str:
        return self.__id

    def set_user_full_name(self, full_name: str):
        self.__user_full_name = full_name

    def get_user_full_name(self) -> str:
        return self.__user_full_name

    def set_user_email_address(self, email_address: str):
        self.__user_email_address = email_address

    def get_user_email_address(self) -> str:
        return self.__user_email_address

    def set_title_of_complain(self, title_of_complain: str):
        self.__title_of_complain = title_of_complain

    def get_title_of_complain(self) -> str:
        return self.__title_of_complain

    def set_status_of_user_complaint(self, status_of_complain: str):
        self.__status_of_user_complaint = status_of_complain

    def get_status_of_user_complaint(self) -> str:
        return self.__status_of_user_complaint

    def get_date_and_time(self) -> DateTime:
        return self.__logged_date_of_complain

    def __str__(self):
        return f"""
            Complaint_Id: {self.__id}
            Complaint_Full_Name: {self.__user_full_name}
            Title_of_Complaint: {self.__title_of_complain}
            Status: {self.__status_of_user_complaint}
            Date/Time: {self.__logged_date_of_complain}"""
