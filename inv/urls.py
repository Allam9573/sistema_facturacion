from django.urls import path
from . import views
urlpatterns = [
    path('', views.categorias, name='categorias'),
    path('nueva/', views.nueva_categoria, name='nueva_categoria'),
    path('api/guardar-categoria/', views.guardar_categoria, name='guardar_categoria'),
    path('<int:id>/', views.editar_categoria, name='editar_categoria'),
    path('api/actualizar/<int:id>/', views.actualizar_categoria, name="actualizar_categoria"),
    path('api/eliminar/<int:id>/', views.eliminar_categoria, name='eliminar_categoria')
]
