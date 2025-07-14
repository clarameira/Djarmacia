"""Views do app farmacia."""

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


from farmacia.api.models import Produto
from farmacia.api.serializers import ProdutoSerializer  


class ProdutoViewSet(viewsets.ModelViewSet):
    """ViewSet para manipular produtos da farmácia."""

    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    permission_classes = [IsAuthenticated]

class NotificationAPIView(APIView):
    """View para enviar notificação por e-mail ao acessar a API."""

    permission_classes = [IsAuthenticated]

    def get(self, request):
        """Envia um e-mail para o usuário autenticado."""
        user_email = request.user.email
        if not user_email:
            return Response({"error": "Usuário não possui email cadastrado."}, status=400)

        send_mail(
            'Notificação de acesso à API',
            'Olá! Você acessou a API com sucesso.',
            'debora.costa22396@alunos.ufersa.edu.br',
            [user_email],
            fail_silently=False,
        )

        return Response({"message": f"E-mail enviado com sucesso para {user_email}"})