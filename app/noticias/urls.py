from django.urls import path
from .views import NoticiaList

urlpatterns = [
    path('', NoticiaList.as_view(), name='noticias'),
]