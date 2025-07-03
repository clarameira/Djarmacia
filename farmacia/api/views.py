"""Views do app farmacia."""

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


from farmacia.api.models import Produto
from farmacia.api.serializers import ProdutoSerializer  


class ProdutoViewSet(viewsets.ModelViewSet):
    """ViewSet para manipular produtos da farmácia."""

    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    permission_classes = [IsAuthenticated]