from django.db import models


class Book(models.Model):
    name = models.TextField(null=False)


class Personnel(models.Model):
    name = models.TextField(null=False)
    email = models.EmailField(null=False)
    phone = models.BigIntegerField(null=False)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, default=Book.objects.first().id)
