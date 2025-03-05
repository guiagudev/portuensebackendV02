from rest_framework import serializers
from .models import Jugador

class JugadorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Jugador
        fields = ['id', 'nombre', 'equipo', 'posicion', 'edad']
