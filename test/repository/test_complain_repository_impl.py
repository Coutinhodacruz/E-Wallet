from unittest import TestCase

from data.model.complain import Complain
from data.repository.complain_repository_impl import ComplainRepositoryImpl


class TestHelpDeskRepositoryImpl(TestCase):

    def test_save_one_complaint(self):
        help_desk_repository = ComplainRepositoryImpl()
        help_desk = Complain()
        help_desk_repository.add(help_desk)
        self.assertEqual(1, help_desk_repository.count())

    def test_two_complaint_can_be_saved(self):
        help_desk_repository = ComplainRepositoryImpl()
        first_complaint = Complain()
        second_complaint = Complain()
        help_desk_repository.add(first_complaint)
        help_desk_repository.add(second_complaint)
        self.assertEqual(2, help_desk_repository.count())

    def test_complaint_can_be_deleted(self):
        help_desk_repository = ComplainRepositoryImpl()
        user_complaint = Complain()
        help_desk_repository.add(user_complaint)
        help_desk_repository.delete(1)
        self.assertEqual(0, help_desk_repository.count())

    def test_one_complaint_can_be_deleted_after_adding_two(self):
        help_desk_repository = ComplainRepositoryImpl()
        first_complaint = Complain()
        second_complaint = Complain()
        help_desk_repository.add(first_complaint)
        help_desk_repository.add(second_complaint)
        print("First complain id -> ", first_complaint.get_id())
        print("First complain id -> ", second_complaint.get_id())
        help_desk_repository.delete(1)
        self.assertEqual(1, help_desk_repository.count())

    def test_find_by_identity_number(self):
        help_desk_repository = ComplainRepositoryImpl()
        complain = Complain()
        help_desk_repository.add(complain)

        self.assertEqual(complain, help_desk_repository.find_complain_by_id(1))
