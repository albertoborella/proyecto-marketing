from django.db import models

class Noticia(models.Model):
    titulo = models.CharField(max_length=150)
    subtitulo = models.CharField(max_length=150, verbose_name='Sub título', blank=True, null=True)
    autor = models.CharField(max_length=150, verbose_name='Autor', blank=True, null=True)
    contenido = models.TextField(blank=True, null=True)
    imagen_1 = models.ImageField(upload_to='imagenes/',blank=True, null=True)
    imagen_2 = models.ImageField(upload_to='imagenes/',blank=True, null=True)
    imagen_3 = models.ImageField(upload_to='imagenes/',blank=True, null=True)
    imagen_4 = models.ImageField(upload_to='imagenes/',blank=True, null=True)
    ordenamiento = models.IntegerField()

    class Meta:
        ordering = ['ordenamiento']
    
    def __str__(self):
        return self.titulo
    



