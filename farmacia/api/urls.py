"""ViewSet para manipular produtos da farmácia."""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from farmacia.api.views import ProdutoViewSet, NotificationAPIView
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'produtos', ProdutoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', include(router.urls)),
    path('api/notification/', NotificationAPIView.as_view(), name='notification'),

    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('api-auth/', include('rest_framework.urls')),
]