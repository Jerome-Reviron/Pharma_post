from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
import requests
from app.models import Flux, D_DATE, D_TYPE_VACCIN, D_LOCATION, F_FLUX

def index(request):
    return render(request, 'index.html')

def lecteur_mp3(request):
    return render(request, 'lecteur_mp3.html')


def ETL_ODS_Flux(request):
    # Récupérer tous les Fluxs
    all_fluxs = Flux.objects.all()

    # Nombre de Fluxs par page
    fluxs_per_page = 10

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
    return render(request, 'ETL_ODS_Flux.html', context)

def ETL_DWH_D_DATE(request):
    # Récupérer tous les dates
    all_dates = D_DATE.objects.all()

    # Nombre de dates par page
    dates_per_page = 10

    # Utiliser la pagination
    paginator = Paginator(all_dates, dates_per_page)
    page = request.GET.get('page')

    try:
        dates = paginator.page(page)
    except PageNotAnInteger:
        # Si la page n'est pas un entier, afficher la première page
        dates = paginator.page(1)
    except EmptyPage:
        # Si la page est hors de portée (par exemple, 9999), afficher la dernière page
        dates = paginator.page(paginator.num_pages)

    context = {'dates': dates}
    return render(request, 'ETL_DWH_D_DATE.html', context)

def ETL_DWH_D_LOCATION(request):
    # Récupérer tous les locations
    all_locations = D_LOCATION.objects.all()

    # Nombre de locations par page
    locations_per_page = 10

    # Utiliser la pagination
    paginator = Paginator(all_locations, locations_per_page)
    page = request.GET.get('page')

    try:
        locations = paginator.page(page)
    except PageNotAnInteger:
        # Si la page n'est pas un entier, afficher la première page
        locations = paginator.page(1)
    except EmptyPage:
        # Si la page est hors de portée (par exemple, 9999), afficher la dernière page
        locations = paginator.page(paginator.num_pages)

    context = {'locations': locations}
    return render(request, 'ETL_DWH_D_LOCATION.html', context)

def ETL_DWH_D_TYPE_VACCIN(request):
    # Récupérer tous les vaccinlabels
    all_vaccinlabels = D_TYPE_VACCIN.objects.all()

    # Nombre de vaccinlabels par page
    vaccinlabels_per_page = 10

    # Utiliser la pagination
    paginator = Paginator(all_vaccinlabels, vaccinlabels_per_page)
    page = request.GET.get('page')

    try:
        vaccinlabels = paginator.page(page)
    except PageNotAnInteger:
        # Si la page n'est pas un entier, afficher la première page
        vaccinlabels = paginator.page(1)
    except EmptyPage:
        # Si la page est hors de portée (par exemple, 9999), afficher la dernière page
        vaccinlabels = paginator.page(paginator.num_pages)

    context = {'vaccinlabels': vaccinlabels}
    return render(request, 'ETL_DWH_D_TYPE_VACCIN.html', context)

def ETL_DWH_F_FLUX(request):
    # Récupérer tous les f_fluxs
    all_f_fluxs = F_FLUX.objects.all()

    # Nombre de f_fluxs par page
    f_fluxs_per_page = 10

    # Utiliser la pagination
    paginator = Paginator(all_f_fluxs, f_fluxs_per_page)
    page = request.GET.get('page')

    try:
        f_fluxs = paginator.page(page)
    except PageNotAnInteger:
        # Si la page n'est pas un entier, afficher la première page
        f_fluxs = paginator.page(1)
    except EmptyPage:
        # Si la page est hors de portée (par exemple, 9999), afficher la dernière page
        f_fluxs = paginator.page(paginator.num_pages)

    context = {'f_fluxs': f_fluxs}
    return render(request, 'ETL_DWH_F_FLUX.html', context)