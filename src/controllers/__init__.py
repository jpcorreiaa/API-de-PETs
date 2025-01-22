class PersonCreatorController:
    def __init__(self, people_repository) -> None:
        self.__people_repository = people_repository
