from django.views.generic import ListView
from .models import Noticia

# Vista de Noticias
class NoticiaList(ListView):
    model = Noticia
    template_name='noticias.html'
