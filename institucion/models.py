from django.db import models


class Especialidad(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    icono = models.CharField(max_length=10, default='</>', help_text='Texto corto o símbolo para la tarjeta')
    activa = models.BooleanField(default=True)
    orden = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['orden', 'nombre']
        verbose_name = 'especialidad'
        verbose_name_plural = 'especialidades'

    def __str__(self):
        return self.nombre


class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    resumen = models.TextField(max_length=300)
    fecha = models.DateField()
    publicada = models.BooleanField(default=True)

    class Meta:
        ordering = ['-fecha']
        verbose_name = 'noticia'
        verbose_name_plural = 'noticias'

    def __str__(self):
        return self.titulo
