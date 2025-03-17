from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JugadorViewSet, CarpetaViewSet
from rest_framework_simplejwt.views import (
        TokenObtainPairView,
        TokenRefreshView,
    )
router = DefaultRouter()
router.register(r'jugadores', JugadorViewSet)
router.register(r'carpetas', CarpetaViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
