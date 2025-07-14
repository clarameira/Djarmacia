"""Serializers do app farmacia."""
from rest_framework import serializers
from farmacia.api.models import Produto  # pylint: disable=import-error

# pylint: disable=too-few-public-methods
class ProdutoSerializer(serializers.ModelSerializer):
    """Serializer para o modelo Produto."""

    class Meta:
        """Serializer para o modelo Produto."""
        model = Produto
        fields = '__all__'
