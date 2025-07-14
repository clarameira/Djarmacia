"""URLs do app farmacia."""
# pylint: disable=import-error
from django.urls import path, include
from rest_framework.routers import DefaultRouter # pylint: disable=no-member
from farmacia.api.views import ProdutoViewSet # pylint: disable=no-member

router = DefaultRouter()
router.register(r'produtos', ProdutoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
