"""Modelos do app farmacia."""

import uuid
from django.db import models


class Produto(models.Model):  # pylint: disable=too-few-public-methods
    """Modelo que representa um produto da farmácia."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    estoque = models.IntegerField()

    def __str__(self):
        """Retorna o nome do produto como representação da instância."""
        return self.nome
