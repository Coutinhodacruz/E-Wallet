from data.model.complain import Complain
from data.repository.complain_repository import ComplainRepository


class ComplainRepositoryImpl(ComplainRepository):
    complains: list[Complain] = []
    counter = 0

    def delete(self, identity_number: int) -> None:
        for complaint in self.complains:
            if complaint.get_id() == identity_number:
                self.complains.remove(complaint)
                self.counter -= 1
                break

    def add(self, complain: Complain) -> Complain:
        if complain.get_id() == "":
            complain.set_id(str(self.generate_complain_id()))
            self.complains.append(complain)

        self.counter += 1
        return complain

    def generate_complain_id(self):
        return self.counter + 1

    def count(self) -> int:
        return self.counter

    def find_complain_by_id(self, identity_number) -> Complain | None:
        for complain in self.complains:
            if complain.get_id() == identity_number:
                return complain
        return None
