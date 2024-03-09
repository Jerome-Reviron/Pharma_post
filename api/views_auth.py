from django.views.generic.base import TemplateView
from django.shortcuts import render
from django.contrib.auth import authenticate
from .serializers import LoginSerializer
from django.http import JsonResponse
from django.contrib.auth import login
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

class LoginView(TemplateView):
    template_name = 'login.html'
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    def get(self, request):
        context = {'detail': 'This is the login view. GET method is allowed.'}
        return render(request, self.template_name, context)

    def post(self, request):
        serializer = LoginSerializer(data=request.POST)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return JsonResponse({'token': token.key}, status=status.HTTP_200_OK)
        else:
            return JsonResponse({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
