from abc import ABC, abstractmethod


class PersonFinderControllerInterface(ABC):
    @abstractmethod
    def find(self, person_info: dict) -> dict:
        pass
