from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from app.models import Flux, D_TYPE_VACCIN, D_DATE, D_LOCATION, F_FLUX
from api.serializers import Flux_Serializer, D_TYPE_VACCIN_Serializer, D_DATE_Serializer, D_LOCATION_Serializer, F_FLUX_Serializer

class BaseAPI(APIView):
    """Base class for API views."""
    model = None
    serializer_class = None
    default_t = 'D_TYPE_VACCIN'

    def get(self, request, pk=None):
        t = request.GET.get('t', None)
        if t:
            try:
                data = eval(t).objects.all()
                count = data.count()
            except AttributeError:
                return Response(data={'error': f'Model {t} not found.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            t = 'D_TYPE_VACCIN'
            data = D_TYPE_VACCIN.objects.all()
            count = data.count()

        serializer = eval(f"{t}_Serializer")(data=data, many=True)
        serializer.is_valid()

        result = {
            't': t,
            'count': count,
            'data': serializer.data,
        }

        return Response(data=result, status=status.HTTP_200_OK)

class API_Operational_Data_Store_Flux(BaseAPI):
    """API for Flux model."""
    model = Flux
    serializer_class = Flux_Serializer
    default_t = 'Flux'

class API_Datawarehouse_D_TYPE_VACCIN(BaseAPI):
    """API for D_TYPE_VACCIN model."""
    model = D_TYPE_VACCIN
    serializer_class = D_TYPE_VACCIN_Serializer
    default_t = 'D_TYPE_VACCIN'

class API_Datawarehouse_D_DATE(BaseAPI):
    """API for D_DATE model."""
    model = D_DATE
    serializer_class = D_DATE_Serializer
    default_t = 'D_DATE'

class API_Datawarehouse_D_LOCATION(BaseAPI):
    """API for D_LOCATION model."""
    model = D_LOCATION
    serializer_class = D_LOCATION_Serializer
    default_t = 'D_LOCATION'

class API_Datawarehouse_F_FLUX(BaseAPI):
    """API for F_FLUX model."""
    model = F_FLUX
    serializer_class = F_FLUX_Serializer
    default_t = 'F_FLUX'
