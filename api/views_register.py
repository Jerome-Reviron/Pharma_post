# views_register.py
from django.shortcuts import render, redirect
from django.http import JsonResponse
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.views.generic import View
from .forms import CustomUserCreationForm

class RegisterView(View):
    template_name = 'register.html'
    form_class = CustomUserCreationForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_staff:
            form = self.form_class()
            return render(request, self.template_name, {'form': form})
        else:
            return redirect('login')

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_staff:
            form = self.form_class(request.POST)
            if form.is_valid():
                user = form.save()
                user.is_staff = True
                user.is_superuser = True
                user.save()
                token, created = Token.objects.get_or_create(user=user)
                return JsonResponse({'message': 'Admin user created successfully', 'token': token.key}, status=status.HTTP_201_CREATED)
            else:
                return JsonResponse({'error': form.errors}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return redirect('login')
