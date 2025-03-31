from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import *
from .serializers import *
from django.contrib.auth import authenticate, login
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated



        
class JugadorViewSet(viewsets.ModelViewSet):
    queryset = Jugador.objects.all()
    serializer_class = JugadorSerializer
    
    permission_classes = [IsAuthenticated]
    
    # Método para obtener las opciones para poblar dropdowns
    @action(detail=False, methods=['get'])
    def opciones(self, request):
        """
        Devuelve las opciones de categoría y subcategorías para poblar dropdowns
        """
        return Response({
            "categorias": Jugador.OPCIONES_CATEGORIA,
            "subcategorias": Jugador.OPCIONES_SUBCATEGORIA,
            "equipos": Jugador.OPCIONES_EQUIPO,
        })

    def get_queryset(self):
        """
        Filtra los jugadores en base a los parámetros 'equipo', 'categoria' y 'subcategoria'
        """
        queryset = super().get_queryset()

    # Obtener los parámetros de consulta
        equipo = self.request.query_params.get('equipo', None)
        categoria = self.request.query_params.get('categoria', None)
        subcategoria = self.request.query_params.get('subcategoria', None)
        nombre = self.request.query_params.get('nombre', None)
        edad_min = self.request.query_params.get('edad_min',None)
        edad_max = self.request.query_params.get('edad_max',None)

    # Aplicar filtros si los parámetros están presentes
        if equipo:
            queryset = queryset.filter(equipo=equipo)
        if categoria:
            queryset = queryset.filter(categoria=categoria)
        if subcategoria:
            queryset = queryset.filter(subcategoria=subcategoria)
        if nombre:
            queryset = queryset.filter(nombre__icontains=nombre)
        if edad_min:
            queryset = queryset.filter(edad__gte=int(edad_min))
        if edad_max:
            queryset = queryset.filter(edad__lte=int(edad_max))

        return queryset

    def perform_update(self, serializer):
        """
        Sobrescribe el método perform_update para agregar validación o depuración antes de guardar
        """
        jugador = serializer.save()  # Guarda el objeto actualizado
        print(f"Jugador {jugador.id} actualizado con éxito")  # Aquí podemos hacer una depuración

class CarpetaInformeViewSet(viewsets.ModelViewSet):
    queryset = CarpetaInformes.objects.all()
    serializer_class = CarpetaInformesSerializer        
class CarpetaViewSet(viewsets.ModelViewSet):
    queryset = Carpeta.objects.all()  # Definir un queryset básico
    serializer_class = CarpetaSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        jugador_id = self.request.query_params.get('jugador_id')
        carpeta_id = self.request.query_params.get('id')

        queryset = Carpeta.objects.all()  # Usar el queryset predeterminado

        if jugador_id:
            queryset = queryset.filter(jugador_id=jugador_id, carpeta_padre=None)  # Solo carpetas raíz

        if carpeta_id:
            queryset = queryset.filter(id=carpeta_id)

        return queryset
class PDFViewSet(viewsets.ModelViewSet): 
      
    queryset = PDF.objects.all()
    serializer_class = PDFSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        # Aquí puedes asignar automáticamente la carpeta al PDF
        carpeta_id = self.request.data.get('carpeta')
        carpeta = Carpeta.objects.get(id=carpeta_id)
        serializer.save(carpeta=carpeta)
        
        
class EventoViewSet (viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    #permission_classes = [IsAuthenticated]
    
    
  #  def perform_create(self, serializer):
   #     serializer.save(creado_por=self.request.user)