from django.db import models

class TareaRegistro(models.Model):
    identificador_tarea = models.AutoField(primary_key=True)
    titulo_tarea = models.CharField(max_length=255)
    descripcion_tarea = models.TextField()

    def __str__(self):
        return self.titulo_tarea
