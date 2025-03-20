from rest_framework import serializers
from .models import Jugador, Carpeta,PDF, Evento

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
    def get_imagen_url(self, obj):
        request = self.context.get("request")
        if obj.imagen:
            return request.build_absolute_uri(obj.imagen.url)
        return None

class CarpetaSerializer(serializers.ModelSerializer):
    subcarpetas = serializers.SerializerMethodField()

    class Meta:
        model = Carpeta
        fields = '__all__'

    def get_subcarpetas(self, obj):
        # Aquí estamos accediendo a las subcarpetas a través de la relación inversa
        # "subcarpetas" es el `related_name` que definimos en `ForeignKey` para la relación recursiva
        return CarpetaSerializer(obj.subcarpetas.all(), many=True).data if obj.subcarpetas.exists() else []


class PDFSerializer(serializers.ModelSerializer):
    class Meta:
        model = PDF
        fields = '__all__'
 
class EventoSerializer(serializers.ModelSerializer):
     class Meta:
         model = Evento
         fields = ['id', 'titulo', 'descripcion', 'fecha_inicio', 'fecha_fin']
        # read_only_fields = ['creado_por']

