from django.views.generic.base import TemplateView
from django.contrib.auth import logout
from django.shortcuts import redirect

class LogoutView(TemplateView):

    def get(self, request):
        logout(request)
        return redirect('/')
