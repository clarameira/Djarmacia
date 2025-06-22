from rest_framework import viewsets
from farmacia.models import Produto
from .serializers import ProdutoSerializer
from rest_framework.permissions import IsAuthenticated

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    permission_classes = [IsAuthenticated]