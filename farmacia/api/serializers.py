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
    # S.O.L.I.D.: LSP - Liskov Substitution Principle
    # ProdutoSerializer herda de ModelSerializer
    # e pode ser usada em qualquer lugar onde se espera um serializer,
    # sem quebrar o comportamento do sistema. Respeita o contrato da superclasse.
