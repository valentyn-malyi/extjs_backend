from django.urls import path
from api.v1.views import Personnel, Book

urlpatterns = [
    path("books/", Book.as_view()),
    path("books/<int:pk>", Book.as_view()),
    path("personnels/", Personnel.as_view()),
    path("personnels/<int:pk>", Personnel.as_view()),
]
