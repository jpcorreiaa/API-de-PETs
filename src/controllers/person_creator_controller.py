import re
from src.models.sqlite.interfaces.ipeople_repository import PeopleRepositoryInterface
from src.models.sqlite.interfaces.ipets_repository import PetsRepositoryInterface


class PersonCreatorController:
    def __init__(self, people_repository: PeopleRepositoryInterface) -> None:
        self._people_repository = people_repository

    def create(self, person_info: dict) -> dict:
        first_name = person_info["first_name"]
        last_name = person_info["last_name"]
        age = person_info["age"]
        pet_id = person_info["pet_id"]

        self.__validate_first_and_last_name(first_name, last_name)
        self.__insert_person_in_db(first_name, last_name, age, pet_id)
        format_response = self.__format_response(person_info)
        return format_response

    def __validate_first_and_last_name(self, first_name: str, last_name: str) -> None:
        # Expressão Regular para caracteres que não são letras
        non_valid_caracteres = re.compile(r"[^a-zA-Z]")

        if non_valid_caracteres.search(first_name) or non_valid_caracteres.search(
            last_name
        ):
            raise Exception("Nome da pessoa inválido!")

    def __insert_person_in_db(
        self, first_name: str, last_name: str, age: int, pet_id: int
    ) -> None:
        self._people_repository.insert_person(first_name, last_name, age, pet_id)

    def __format_response(self, person_info: dict) -> dict:
        return {"data": {"type": "Person", "count": 1, "attributes": person_info}}