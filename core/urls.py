from django.urls import path

from .views import home, generate_password

urlpatterns = [
    path('', generate_password, name='gerador'),
    path('', home, name='home'),
]

