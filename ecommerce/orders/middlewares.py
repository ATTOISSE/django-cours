from typing import Any


class HeaderMiddleware:
    def __init__(self,get_response) -> None:
        self.get_response = get_response

    def __call__(self, request) -> Any:
        print("Avant requete")
        response = self.get_response(request)
        print('Aprés requete')
        return response
