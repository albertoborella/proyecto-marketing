# Generated by Django 4.1 on 2023-07-14 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0003_remove_noticia_contenido_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='noticia',
            name='contenido',
        ),
        migrations.RemoveField(
            model_name='noticia',
            name='fecha_publicacion',
        ),
    ]
