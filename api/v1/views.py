from django.views import View
from django.http import JsonResponse
from django.core.handlers.wsgi import WSGIRequest
from api.v1.models import Personnel as PersonnelModel, Book
import json


class Personnels(View):
    # noinspection PyMethodMayBeStatic
    def get(self, request: WSGIRequest):
        data = {
            "status": "OK",
            "data": list(PersonnelModel.objects.values())
        }
        return JsonResponse(data=data)


class Books(View):
    # noinspection PyMethodMayBeStatic
    def get(self, request: WSGIRequest):
        data = {
            "status": "OK",
            "data": list(Book.objects.values())
        }
        return JsonResponse(data=data)


class Personnel(View):
    # noinspection PyMethodMayBeStatic
    def get(self, request: WSGIRequest, _id: int):
        personnels = PersonnelModel.objects.values().get(pk=_id)
        data = {
            "status": "OK",
            "data": personnels
        }
        return JsonResponse(data=data)

    # noinspection PyMethodMayBeStatic
    def post(self, request: WSGIRequest):
        data = {"status": 200}
        # sleep(5)
        return JsonResponse(data=data)

    # noinspection PyMethodMayBeStatic
    def put(self, request: WSGIRequest, _id: int):
        body = json.loads(request.body)
        if body.get("name", "").startswith("s"):
            data = {
                "status": "ERROR",
                "message": "name can't start with s"
            }
            return JsonResponse(data=data)

        PersonnelModel.objects.filter(pk=_id).update(**body)
        data = {
            "status": "OK",
            "message": "Update complete"
        }
        return JsonResponse(data=data)

    # noinspection PyMethodMayBeStatic
    def delete(self, request: WSGIRequest):
        data = {"status": 200}
        # sleep(5)
        return JsonResponse(data=data)
