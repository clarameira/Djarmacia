"""Views do app farmacia."""

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.core.mail import send_mail
from django.conf import settings
from farmacia.api.models import Produto
from farmacia.api.serializers import ProdutoSerializer


class ProdutoViewSet(viewsets.ModelViewSet): # pylint: disable=too-many-ancestors
    """ViewSet para manipular produtos da farmácia."""
    queryset = Produto.objects.all() # pylint: disable=no-member
    serializer_class = ProdutoSerializer
    permission_classes = [IsAuthenticated]
# S.O.L.I.D.: OCP - Open/Closed Principle
# Essa classe estende o ModelViewSet do DRF sem modificar o código interno da superclasse.
# Está "aberta para extensão" (ao sobrescrever métodos como create/update futuramente) e
#  "fechada para modificação".

class NotificationAPIView(APIView):
    """View para enviar notificação por e-mail ao acessar a API."""
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """Envia notificação por e-mail para o usuário autenticado."""
        user_email = request.user.email
        if not user_email:
            return Response({"error": "Usuário não possui email cadastrado."}, status=400)

        send_mail(
            'Notificação de acesso à API',
            'Olá! Você acessou a API com sucesso.',
            settings.DEFAULT_FROM_EMAIL,
            [user_email],
            fail_silently=False,
        )
        return Response(
            {"message": f"E-mail enviado com sucesso para {user_email}"}
        )

# S.O.L.I.D.: SRP - Single Responsibility Principle (violado)
# Essa view está tratando tanto da lógica de envio de e-mail quanto da lógica HTTP da view.
