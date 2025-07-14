"""ViewSet para manipular produtos da farmácia."""
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.core.mail import send_mail
from farmacia.api.models import Produto
from farmacia.api.serializers import ProdutoSerializer
from django.conf import settings


class ProdutoViewSet(viewsets.ModelViewSet):
    """ViewSet para manipular produtos da farmácia."""
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    permission_classes = [IsAuthenticated]


class NotificationAPIView(APIView):
    """ViewSet para manipular produtos da farmácia."""
    permission_classes = [IsAuthenticated]

    def post(self, request):
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
        return Response({"message": f"E-mail enviado com sucesso para {user_email}"})
    