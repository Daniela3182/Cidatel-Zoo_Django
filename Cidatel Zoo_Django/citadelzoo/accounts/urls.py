from django.urls import path
from .views import simple_login, simple_logout

urlpatterns = [
    path('ingresar/', simple_login, name='simple_login'),
    path('salir/', simple_logout, name='simple_logout'),
]
