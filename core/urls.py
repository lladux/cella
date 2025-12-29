from django.urls import path
from .views import *

app_name = "core"

urlpatterns=[
    path('', index, name='index'),
    path('login', InicioSeion.as_view(), name='login'),
    path('log_out', cierre, name='log_out'),
    path('join', Registro.as_view(), name='join'),
    path('staff', AdminIndex.as_view(), name='staff'),
]