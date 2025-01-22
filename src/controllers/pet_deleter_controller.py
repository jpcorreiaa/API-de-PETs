from .interfaces.ipet_deleter_controller import PetDeleterControllerInterface
from src.models.sqlite.entities.pets import PetsTable
from src.models.sqlite.interfaces.ipets_repository import PetsRepositoryInterface


class PetDeleterController(PetDeleterControllerInterface):
    def __init__(self, pet_repository: PetsRepositoryInterface) -> None:
        self.__pet_repository = pet_repository

    def delete(self, name: str) -> None:
        self.__pet_repository.delete_pets(name)
