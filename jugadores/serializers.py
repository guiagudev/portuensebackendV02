from rest_framework import serializers
from .models import Jugador, Carpeta,PDF

class JugadorSerializer(serializers.ModelSerializer):
    # Usamos ChoiceField para los campos
    categoria = serializers.ChoiceField(choices=Jugador.OPCIONES_CATEGORIA)
    subcategoria = serializers.ChoiceField(choices=Jugador.OPCIONES_SUBCATEGORIA)
    equipo = serializers.ChoiceField(choices=Jugador.OPCIONES_EQUIPO)

    class Meta:
        model = Jugador
        fields = '__all__'

    def to_representation(self, instance):
        """
        Modificamos la representación para que devuelva los valores legibles,
        en lugar de los valores internos de la base de datos.
        """
        representation = super().to_representation(instance)
        # Convertir las claves a valores legibles
        representation['categoria'] = dict(Jugador.OPCIONES_CATEGORIA).get(instance.categoria, instance.categoria)
        representation['subcategoria'] = dict(Jugador.OPCIONES_SUBCATEGORIA).get(instance.subcategoria, instance.subcategoria)
        representation['equipo'] = dict(Jugador.OPCIONES_EQUIPO).get(instance.equipo, instance.equipo)
        return representation 

class CarpetaSerializer(serializers.ModelSerializer):
    subcarpetas = serializers.SerializerMethodField()

    class Meta:
        model = Carpeta
        fields = ['id', 'nombre', 'carpeta_padre', 'subcarpetas']

    def get_subcarpetas(self, obj):
        return CarpetaSerializer(obj.subcarpetas.all(), many=True).data

class PDFSerializer(serializers.ModelSerializer):
    class Meta:
        model = PDF
        fields = '__all__'