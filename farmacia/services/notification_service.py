from django.core.mail import send_mail
from django.conf import settings

class EmailNotifier:
    """Responsável por enviar notificações por e-mail."""

    def __init__(self, destinatario):
        self.destinatario = destinatario

    def enviar_notificacao(self, assunto, mensagem):
        send_mail(
            assunto,
            mensagem,
            settings.DEFAULT_FROM_EMAIL,
            [self.destinatario],
            fail_silently=False,
        )