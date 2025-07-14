"""Modelos do app farmacia."""

import uuid
from django.db import models

# pylint: disable=too-few-public-methods
class Produto(models.Model):
    """Modelo que representa um produto da farmácia."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    estoque = models.IntegerField()

    def __str__(self):
        """Retorna o nome do produto como representação da instância."""
        return str(self.nome) if self.nome is not None else ''
# S.O.L.I.D.: SRP - Single Responsibility Principle
# A classe Produto tem apenas uma responsabilidade: representar os dados de um produto.
# Qualquer lógica de negócio, como cálculo de descontos ou relatórios, deve ser feita fora daqui.
