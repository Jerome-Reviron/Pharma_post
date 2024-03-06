from django.urls import path
from api.views_auth import LoginView
from api.views import API_Operational_Data_Store_Flux, API_Datawarehouse_D_TYPE_VACCIN, API_Datawarehouse_D_DATE, API_Datawarehouse_D_LOCATION, API_Datawarehouse_F_FLUX

urlpatterns = [
    path('ODS/', API_Operational_Data_Store_Flux.as_view(), name='api_operational_data_store_flux'),
    path('ODS/<int:id>/', API_Operational_Data_Store_Flux.as_view(), name='api_operational_data_store_flux_detail'),
    path('DWH/D_TYPE_VACCIN/', API_Datawarehouse_D_TYPE_VACCIN.as_view(), name='api_datawarehouse_d_type_vaccin'),
    path('DWH/D_TYPE_VACCIN/<str:vaccinlabel>/', API_Datawarehouse_D_TYPE_VACCIN.as_view(), name='api_datawarehouse_d_type_vaccin_detail'),
    path('DWH/D_DATE/', API_Datawarehouse_D_DATE.as_view(), name='api_datawarehouse_d_date'),
    path('DWH/D_DATE/<str:date_fin_semaine>/', API_Datawarehouse_D_DATE.as_view(), name='api_datawarehouse_d_date_detail'),
    path('DWH/D_LOCATION/', API_Datawarehouse_D_LOCATION.as_view(), name='api_datawarehouse_d_location'),
    path('DWH/D_LOCATION/<str:code_region_code_departement>/', API_Datawarehouse_D_LOCATION.as_view(), name='api_datawarehouse_d_location_detail'),
    path('DWH/F_FLUX/', API_Datawarehouse_F_FLUX.as_view(), name='api_datawarehouse_f_flux'),
    path('DWH/F_FLUX/<str:PK_F_FLUX>/', API_Datawarehouse_F_FLUX.as_view(), name='api_datawarehouse_f_flux_detail'),
    path('DWH_ALL/', API_Datawarehouse_D_TYPE_VACCIN.as_view()),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    ]