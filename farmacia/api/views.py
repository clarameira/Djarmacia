"""Views do app farmacia."""
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from farmacia.api.models import Produto  # pylint: disable=import-error
from farmacia.api.serializers import ProdutoSerializer  # pylint: disable=import-error


class ProdutoViewSet(viewsets.ModelViewSet):  # pylint: disable=too-many-ancestors
    """ViewSet para manipular produtos da farmácia."""

    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    permission_classes = [IsAuthenticated]
