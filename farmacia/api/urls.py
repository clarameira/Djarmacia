"""URLs do app farmacia."""

from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .views import ProdutoViewSet, NotificationAPIView

router = DefaultRouter()
router.register(r'produtos', ProdutoViewSet)

urlpatterns = router.urls + [
    path('notification/', NotificationAPIView.as_view(), name='notification'),
    path('token/', obtain_auth_token, name='api_token_auth'),
]
