"""
Serializers do app 'farmacia'. Define classes de serialização para o modelo Produto,
seguindo os princípios SOLID.
"""

from rest_framework import serializers
from farmacia.api.models import Produto

class ProdutoBaseSerializer(serializers.ModelSerializer):
    """
    SRP (Single Responsibility Principle):
    - Essa classe tem a única responsabilidade de serializar o modelo Produto.
    - Não contém validações específicas nem lógica extra.
    - Serve como base para outros serializers que podem adicionar funcionalidades.
    """
    class Meta:
        """Class representing a person"""
        # pylint: disable=too-few-public-methods
        model = Produto
        fields = '__all__'


class ProdutoCreateSerializer(ProdutoBaseSerializer):
    """
    OCP (Open/Closed Principle):
    - Essa classe estende ProdutoBaseSerializer para adicionar validações específicas de criação,
      sem modificar a classe base.
    - Está aberta para extensão (adicionar validações), mas fechada para modificação da base.
    
    SRP:
    - Responsável apenas por regras de validação para criação.
    """
    def validate_nome(self, value):
        """Valida se o nome do produto não está vazio."""
        if not value:
            raise serializers.ValidationError("Nome do produto não pode ser vazio.")
        return value


class ProdutoDetailSerializer(ProdutoBaseSerializer):
    """
    ISP (Interface Segregation Principle):
    - Oferece uma interface específica para exibir detalhes do produto.
    - Adiciona apenas o campo extra 'preco_com_desconto' relevante para visualização detalhada,
      evitando que o serializer base fique inchado com funcionalidades que nem todo uso precisa.
    
    SRP:
    - Responsável apenas por apresentar dados para visualização detalhada.
    """
    preco_com_desconto = serializers.SerializerMethodField()

    def get_preco_com_desconto(self, obj):
        """Calcula o preço com desconto de 10%."""
        # Exemplo de cálculo
        return obj.preco * 0.9


# LSP (Liskov Substitution Principle): Todos os serializers
# podem ser usados onde ModelSerializer é esperado.
# DIP (Dependency Inversion Principle): A dependência
# com o modelo Produto é direta, mas aceitável no contexto.
