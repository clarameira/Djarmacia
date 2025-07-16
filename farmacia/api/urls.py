"""URLs do app farmacia."""

from django.contrib import admin
from django.urls import path, include

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from farmacia.api.views import ProdutoViewSet, NotificationAPIView


router = DefaultRouter()
router.register(r'produtos', ProdutoViewSet)

urlpatterns = [
    # normalmente essa rota fica no core/urls.py, mas se quiser aqui pode
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/notification/', NotificationAPIView.as_view(), name='notification'),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('api-auth/', include('rest_framework.urls')),
]
