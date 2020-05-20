from django.db import models


class Personnel(models.Model):
    name = models.TextField(null=False)
    email = models.EmailField(null=False)
    phone = models.BigIntegerField(null=False)



class Book(models.Model):
    name = models.TextField(null=False)