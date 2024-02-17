from django.db import models
from app.models import ClaseModelo
# Create your models here.


class Categoria(ClaseModelo):
    descripcion = models.CharField(
        max_length=100, help_text='Descripcion Categoria', unique=True)

    def __str__(self):
        return f'{self.descripcion}'

    class Meta:
        verbose_name_plural = 'Categorias'
