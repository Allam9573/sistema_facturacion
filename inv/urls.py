from django.urls import path
from . import views
urlpatterns = [
    path('', views.categorias, name='categorias'),
    path('nueva/', views.nueva_categoria, name='nueva_categoria'),
    path('api/guardar-categoria/', views.guardar_categoria, name='guardar_categoria')
]
