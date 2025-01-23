from http_types.http_response import HttpResponse
from interfaces.view_interface import ViewInterface
from src.controllers.interfaces.ipet_deleter_controller import (
    PetDeleterControllerInterface,
)
from src.views.http_types.http_request import HttpRequest


class PetDeleterView(ViewInterface):
    def __init__(self, controller: PetDeleterControllerInterface) -> None:
        self._controller = controller

    def handle(self, http_request: HttpRequest) -> HttpResponse:
        name = http_request.param["name"]
        self._controller.delete(name)
        return HttpResponse(status_code=204)
