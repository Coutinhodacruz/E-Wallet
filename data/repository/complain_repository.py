from data.model.complain import Complain


class ComplainRepository:
    def add(self, complain: Complain):
        raise NotImplementedError

    def count(self) -> int:
        raise NotImplementedError

    def delete(self, delete_by_id: int) -> None:
        raise NotImplementedError

    def find_complain_by_id(self, identity_number):
        raise NotImplementedError
