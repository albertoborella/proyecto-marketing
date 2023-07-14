from django.urls import path
from .views import ServicioList

urlpatterns = [
    path('', ServicioList.as_view(), name='servicios'),
]