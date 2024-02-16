from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('sign/', views.sign_up, name='sign'),
    path('api/register/', views.add_user, name='add_user')
]
