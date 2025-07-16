"""Interfaces de serviços do sistema."""

from abc import ABC, abstractmethod

# S.O.L.I.D.: DIP (Princípio da Inversão de Dependência)
# Interface que define o contrato de qualquer serviço de notificação
class Notifier(ABC):
    @abstractmethod
    def enviar_notificacao(self, assunto, mensagem):
        pass