from unittest import TestCase
from xmlrpc.client import DateTime

from dtos.request.complain_request import ComplainRequest
from services.complain_service_impl import ComplainServiceImpl


class TestComplainServiceImpl(TestCase):
    complain_service = ComplainServiceImpl()

    def test_user_can_log_complain(self):
        complain_request = ComplainRequest()
        complain_request.set_user_full_name("Zainab Shoper")
        complain_request.set_user_email_address("zainab-shoper@gmail.com")
        complain_request.set_title_of_complain("Unauthorized Debit")
        current_date_and_time = complain_request.get_date_and_time()
        complain_request.set_body_of_complain("""
        It has become a reoccurring act for instant pay to always 
        debit #200.50 on my account every week. This act feels
        unreasonable and I would like to close my account with immediate effect.
        """)

        expected = f"""
            Complaint_Id: 1
            Complaint_Full_Name: Zainab Shoper
            Title_of_Complaint: Unauthorized Debit
            Status: UNASSIGNED
            Date/Time: {current_date_and_time}"""
        self.assertEqual(expected, self.complain_service.log_complain(complain_request).__str__())

    def test_user_can_track_complain_with_id(self):
        complain_request = ComplainRequest()
        complain_request.set_user_full_name("Zainab Shoper")
        complain_request.set_user_email_address("zainab-shoper@gmail.com")
        complain_request.set_title_of_complain("Bad Network")
        complain_request.set_body_of_complain("""
                           I feel Instant pay should work on their network""")
        self.complain_service.log_complain(complain_request)

        expected = "Complaint resolved"
        self.assertEqual(expected, self.complain_service.check_complain_status(1))
