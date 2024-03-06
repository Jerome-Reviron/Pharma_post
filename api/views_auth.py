from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.contrib.auth import authenticate
from .serializers import LoginSerializer
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import AllowAny

class LoginView(TemplateView):
    template_name = 'login.html'
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [AllowAny]

    def get(self, request):
        context = {'detail': 'This is the login view. GET method is allowed.'}
        return render(request, self.template_name, context)

    def post(self, request):
        serializer = LoginSerializer(data=request.POST)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            token, created = Token.objects.get_or_create(user=user)
            return JsonResponse({'token': token.key}, status=status.HTTP_200_OK)
        else:
            # En cas d'erreur de validation du sérialiseur, renvoyer une réponse JSON avec le statut 400
            return JsonResponse({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
