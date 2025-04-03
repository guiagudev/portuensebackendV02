from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *
from rest_framework_simplejwt.views import (
        TokenObtainPairView,
        TokenRefreshView,
    )
router = DefaultRouter()
router.register(r'jugadores', JugadorViewSet)
router.register(r'carpetas', CarpetaViewSet, basename='carpeta')
router.register(r'pdfs',PDFViewSet)
router.register(r'eventos',EventoViewSet)
router.register(r'folders', FolderGroupViewSet)
router.register(r'files', ExcelFileViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
