from django.db import models

# MODELOS DE SERVICIOS
class Servicio(models.Model):
    titulo = models.CharField(max_length=150, unique=True)
    texto = models.TextField(blank=True, null=True)
    imagen = models.ImageField(upload_to='servicios/',blank=True, null=True)
    ordenamiento = models.IntegerField()

    class Meta:
        ordering = ['ordenamiento']

    def __str__(self):
        return self.titulo


