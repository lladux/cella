from django.urls import path
from .views import *

app_name = "core"
# Create your views here.

urlpatterns=[
    path('', index, name='index'),
    path('login', InicioSecion.as_view(), name='inicisesion'),
    path('cierre', cierre, name='cierre'),
    path('api', LoginApi.as_view())

]