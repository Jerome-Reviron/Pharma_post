from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
import requests
from app.models import Flux

def index(request):
    # Récupérer tous les fluxs
    all_fluxs = Flux.objects.all()

    # Nombre de fluxs par page
    fluxs_per_page = 7

    # Utiliser la pagination
    paginator = Paginator(all_fluxs, fluxs_per_page)
    page = request.GET.get('page')

    try:
        fluxs = paginator.page(page)
    except PageNotAnInteger:
        # Si la page n'est pas un entier, afficher la première page
        fluxs = paginator.page(1)
    except EmptyPage:
        # Si la page est hors de portée (par exemple, 9999), afficher la dernière page
        fluxs = paginator.page(paginator.num_pages)

    context = {'fluxs': fluxs}
    return render(request, 'index.html', context)
