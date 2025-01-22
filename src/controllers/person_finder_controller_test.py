import pytest
from src.controllers.person_finder_controller import PersonFinderController


class MockPerson:
    def __init__(self, first_name, last_name, pet_name, pet_type) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.pet_name = pet_name
        self.pet_type = pet_type


class MockPeopleRepository:
    def get_person(self, person_id: int):
        return MockPerson(
            first_name="John", last_name="Doe", pet_name="Fluffy", pet_type="dog"
        )


def test_find():

    controller = PersonFinderController(MockPeopleRepository())
    response = controller.find(123)

    expected_response = {
        "data": {
            "type": "Person",
            "count": 1,
            "attributes": {
                "first_name": "John",
                "last_name": "Doe",
                "pet_name": "Fluffy",
                "pet_type": "dog",
            },
        }
    }

    assert response == expected_response


# def test_find_error():
#     person_info = {
#         "first_name": "Fulano123",
#         "last_name": "deTal",
#         "age": 30,
#         "pet_id": 123,
#     }

#     controller = PersonCreatorController(MockPeopleRepository())

#     with pytest.raises(Exception):
#         controller.create(person_info)
