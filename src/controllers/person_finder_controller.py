from typing import Dict
from .interfaces.iperson_finder_controller import PersonFinderControllerInterface
from src.models.sqlite.interfaces.ipeople_repository import PeopleRepositoryInterface
from src.models.sqlite.entities.people import PeopleTable


class PersonFinderController(PersonFinderControllerInterface):
    def __init__(self, people_repository: PeopleRepositoryInterface) -> None:
        self._people_repository = people_repository

    def find(self, person_id: int) -> Dict:
        person = self.__find_person_in_db(person_id)
        format_response = self.__format_response(person)
        return format_response

    def __find_person_in_db(self, person_id: int) -> PeopleTable:
        person = self._people_repository.get_person(person_id)
        if not person:
            raise Exception("Pessoa nao encontrada!")

        return person

    def __format_response(self, person: PeopleTable) -> Dict:
        return {
            "data": {
                "type": "Person",
                "count": 1,
                "attributes": {
                    "first_name": person.first_name,
                    "last_name": person.last_name,
                    "pet_name": person.pet_name,
                    "pet_type": person.pet_type,
                },
            }
        }
