from django.views.generic import ListView
from .models import Servicio

# Vista de Inicio
class ServicioList(ListView):
    model = Servicio
    template_name='servicios.html'



