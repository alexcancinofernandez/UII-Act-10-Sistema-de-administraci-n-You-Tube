from django.db import models

class Video(models.Model):
    id_video = models.CharField(max_length=50, unique=True)
    id_canal = models.CharField(max_length=50)
    titulo = models.CharField(max_length=200)
    fecha_subida = models.DateField()
    duracion = models.DurationField()
    vistas = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.titulo} ({self.id_video})"
