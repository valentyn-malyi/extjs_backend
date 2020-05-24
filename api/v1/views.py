from django.views import View
from django.http import JsonResponse
from django.core.handlers.wsgi import WSGIRequest
from api.v1.models import Personnel as PersonnelModel, Book as BookModel
import json


class Book(View):
    # noinspection PyMethodMayBeStatic
    def get(self, request: WSGIRequest):
        data = {
            "status": "OK",
            "data": list(BookModel.objects.values())
        }
        return JsonResponse(data=data)

    # noinspection PyMethodMayBeStatic
    def put(self, request: WSGIRequest, pk: int):
        body = json.loads(request.body)
        if not body.get("name"):
            data = {
                "status": "ERROR",
                "message": "Empty name"
            }
            return JsonResponse(data=data)

        BookModel.objects.filter(pk=pk).update(**body)
        data = {
            "status": "OK",
            "message": "Update complete"
        }
        return JsonResponse(data=data)


class Personnel(View):
    # noinspection PyMethodMayBeStatic
    def get(self, request: WSGIRequest, pk: int = None):
        if pk is None:
            personnels = list(PersonnelModel.objects.values())
        else:
            personnels = PersonnelModel.objects.values().get(pk=pk)
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
    def put(self, request: WSGIRequest, pk: int):
        body = json.loads(request.body)
        if body.get("name","no s ").startswith("s"):
            data = {
                "status": "ERROR",
                "message": "name can't start with s"
            }
            return JsonResponse(data=data)

        PersonnelModel.objects.filter(pk=pk).update(**body)
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
