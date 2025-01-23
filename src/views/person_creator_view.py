from http_types.http_request import HttpRequest
from http_types.http_response import HttpResponse
from interfaces.view_interface import ViewInterface
from src.controllers.interfaces.iperson_creator_controller import (
    PersonCreatorControllerInterface,
)


class PersonCreatorView(ViewInterface):
    def __init__(self, controller: PersonCreatorControllerInterface) -> None:
        self._controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        person_info = http_request.body
        body_response = self.controller.create(person_info)

        return HttpResponse(status_code=201, body=body_response)
