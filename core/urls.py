from django.urls import path

from . import views
from .views import home

urlpatterns = [
    path('', views.generate_password, name='gerador'),
    path('gerador/', views.generate_password, name='gerador'),
    path('gerador/', home, name='home'),
]

