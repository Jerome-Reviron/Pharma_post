from django.urls import path
from api.views import API_Operational_Data_Store_Flux, API_Datawarehouse_D_TYPE_VACCIN, API_Datawarehouse_D_DATE, API_Datawarehouse_D_LOCATION, API_Datawarehouse_F_FLUX

urlpatterns = [
    path('ODS/', API_Operational_Data_Store_Flux.as_view()),
    path('DWH/D_TYPE_VACCIN/', API_Datawarehouse_D_TYPE_VACCIN.as_view()),
    path('DWH/D_DATE/', API_Datawarehouse_D_DATE.as_view()),
    path('DWH/D_LOCATION/', API_Datawarehouse_D_LOCATION.as_view()),
    path('DWH/F_FLUX/', API_Datawarehouse_F_FLUX.as_view()),
]