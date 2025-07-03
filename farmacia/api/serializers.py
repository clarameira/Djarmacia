"""Serializers do app farmacia."""

from rest_framework import serializers
from farmacia.api.models import Produto


class ProdutoSerializer(serializers.ModelSerializer):
    """Serializer para o modelo Produto."""

    class Meta:
        """class Meta."""
        model = Produto
        fields = '__all__'

