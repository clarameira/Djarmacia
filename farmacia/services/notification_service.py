from django.core.mail import send_mail
from django.conf import settings

# S.O.L.I.D.: SRP – Single Responsibility Principle
# Esta classe tem uma única responsabilidade: enviar notificações por e-mail.
# Ela não lida com requisições HTTP, lógica de negócios ou qualquer outra funcionalidade.
class EmailNotifier:
    """Responsável por enviar notificações por e-mail."""

    def __init__(self, destinatario):
        # S.O.L.I.D.: DIP – Dependency Inversion Principle (parcialmente)
        # A dependência do e-mail está encapsulada: a classe recebe o destinatário de fora,
        # o que facilita a substituição da origem dos dados em testes ou variações de uso.
        self.destinatario = destinatario

    def enviar_notificacao(self, assunto, mensagem):
        send_mail(
            assunto,
            mensagem,
            settings.DEFAULT_FROM_EMAIL,
            [self.destinatario],
            fail_silently=False,
        )
