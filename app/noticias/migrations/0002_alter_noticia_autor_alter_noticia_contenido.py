# Generated by Django 4.1 on 2023-07-13 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('noticias', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='noticia',
            name='autor',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Autor'),
        ),
        migrations.AlterField(
            model_name='noticia',
            name='contenido',
            field=models.TextField(blank=True, null=True),
        ),
    ]
