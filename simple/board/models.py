from django.db import models
from django.contrib.auth.models import User
from django.views.generic import TemplateView



class Board(models.model):
    name = models.model(CharField=100, unique=True)
    description = models.model((CharField= 200)


# Create your models here.
