from rest_framework import serializers
from .models import TareaRegistro

class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = TareaRegistro
        fields = ['identificador_tarea', 'titulo_tarea', 'descripcion_tarea']
