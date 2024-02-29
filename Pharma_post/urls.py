"""
URL configuration for Pharma_post project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import index
from app.views import ETL_ODS_Flux
from app.views import ETL_DWH_D_DATE
from app.views import ETL_DWH_D_LOCATION
from app.views import ETL_DWH_D_TYPE_VACCIN
from app.views import ETL_DWH_F_FLUX



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('ETL_ODS_Flux/', ETL_ODS_Flux),
    path('ETL_DWH_D_DATE/', ETL_DWH_D_DATE),
    path('ETL_DWH_D_LOCATION/', ETL_DWH_D_LOCATION),
    path('ETL_DWH_D_TYPE_VACCIN/', ETL_DWH_D_TYPE_VACCIN),
    path('ETL_DWH_F_FLUX/', ETL_DWH_F_FLUX),
]
