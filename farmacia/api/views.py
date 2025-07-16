"""Views do app farmacia."""

from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response

from farmacia.api.models import Produto
from farmacia.api.serializers import ProdutoBaseSerializer
from farmacia.services.notification_service import EmailNotifier  # DIP: depende de abstração

# S.O.L.I.D.: SRP (Princípio da Responsabilidade Única)
# Esta view trata apenas da manipulação dos produtos.
# Toda a lógica relacionada ao modelo está no serializer e ao banco no model.
class ProdutoViewSet(viewsets.ModelViewSet):  # pylint: disable=too-many-ancestors
    """ViewSet para manipular produtos da farmácia."""
    queryset = Produto.objects.all()  # pylint: disable=no-member
    serializer_class = ProdutoBaseSerializer
    permission_classes = [AllowAny]

    # S.O.L.I.D.: OCP (Princípio Aberto/Fechado)
    # Podemos estender esse método para adicionar lógica ao salvar sem modificar a superclasse.
    def perform_create(self, serializer):
        # lógica extra (ex: log, notificação, validação) pode ser adicionada aqui
        serializer.save()


# S.O.L.I.D.: SRP (Princípio da Responsabilidade Única)
# Esta view só gerencia a requisição HTTP.
# A lógica de envio de e-mail está encapsulada em uma classe separada.
class NotificationAPIView(APIView):
    """View para enviar notificação por e-mail ao acessar a API."""
    permission_classes = [IsAuthenticated]

    def post(self, request):
        """Envia notificação por e-mail para o usuário autenticado."""
        user_email = request.user.email
        if not user_email:
            return Response({"error": "Usuário não possui email cadastrado."}, status=400)

        # S.O.L.I.D.: DIP (Princípio da Inversão de Dependência)
        # A view depende de uma abstração (EmailNotifier),
        # não da implementação concreta (send_mail).
        notifier = EmailNotifier(user_email)
        notifier.enviar_notificacao(
            'Notificação de acesso à API',
            'Olá! Você acessou a API com sucesso.'
        )

        return Response({"message": f"E-mail enviado com sucesso para {user_email}"})
