from src.models.sqlite.interfaces.ipeople_repository import PeopleRepositoryInterface
from src.models.sqlite.interfaces.ipets_repository import PetsRepositoryInterface


class PersonCreatorController:
    def __init__(self, people_repository: PeopleRepositoryInterface) -> None:
        self._people_repository = people_repository

    def __init__(self, pets_repository: PetsRepositoryInterface) -> None:
        self._pets_repository = pets_repository
