from django.urls import path

from .views import home, generate_password

app_name = 'core'

urlpatterns = [
    path('', generate_password, name='gerador'),
    path('gerador/', home, name='home'),
]

