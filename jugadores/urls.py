from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JugadorViewSet, CarpetaViewSet
router = DefaultRouter()
router.register(r'jugadores', JugadorViewSet)
router.register(r'carpetas', CarpetaViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
