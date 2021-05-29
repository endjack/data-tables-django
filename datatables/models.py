from django.contrib import admin
from django.db import models

# Create your models here.

class Cliente(models.Model):
    nome = models.CharField(max_length=200)
    telefone = models.CharField(max_length=20)





admin.site.register(Cliente)