from django.urls import path
from api.v1.views import Personnels, Personnel, Books

urlpatterns = [
    path("books/", Books.as_view()),
    path("personnels/", Personnels.as_view()),
    path("personnels/<int:_id>", Personnel.as_view()),
]
