from django.db import models

# MODELO PAGINA DE INICIO
class Inicio(models.Model):
    title = models.CharField(max_length=150, verbose_name='Título', default='Modifica el título')
    imagen = models.ImageField(upload_to='imagenes/', blank=True, null=True)
    texto = models.TextField(blank=True, null=True)
    ordenamiento = models.IntegerField(verbose_name='Nº de órden')

    class Meta:
        ordering = ['ordenamiento']
        verbose_name = 'Dato de página de inicio'
        verbose_name_plural = 'Datos de página de inicio'

    def __str__(self):
        return self.title
    

