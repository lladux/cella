from django.urls import path
from .views import *

app_name = "core"
# Create your views here.

urlpatterns=[
    path('', index, name='index'),
    path('login', InicioSeion.as_view(), name='login'),
    path('cierre', cierre, name='cierre'),
    path('join', Registro.as_view(), name='join'),
    path('staff', AdminIndex.as_view(), name='staff'),
]