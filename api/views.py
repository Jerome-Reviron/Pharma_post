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

    def get(self, request, pk=None, *args, **kwargs):
        t = kwargs.get('t', self.default_t)
        model = getattr(self, f'model_{t}', None)

        if not model:
            return Response(data={'error': f'Model {t} not found.'}, status=status.HTTP_400_BAD_REQUEST)

        data = model.objects.all()
        count = data.count()

        serializer = getattr(self, f'serializer_{t}', None)

        if not serializer:
            return Response(data={'error': f'Serializer for model {t} not found.'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = serializer(data=data, many=True)
        serializer.is_valid()

        result = {
            't': t,
            'count': count,
            'data': serializer.data,
        }

        return Response(data=result, status=status.HTTP_200_OK)

class API_Operational_Data_Store_Flux(BaseAPI):
    """API for Flux model."""
    model_Flux = Flux
    serializer_Flux = Flux_Serializer
    default_t = 'Flux'

class API_Datawarehouse_D_TYPE_VACCIN(BaseAPI):
    """API for D_TYPE_VACCIN model."""
    model_D_TYPE_VACCIN = D_TYPE_VACCIN
    serializer_D_TYPE_VACCIN = D_TYPE_VACCIN_Serializer
    default_t = 'D_TYPE_VACCIN'

class API_Datawarehouse_D_DATE(BaseAPI):
    """API for D_DATE model."""
    model_D_DATE = D_DATE
    serializer_D_DATE = D_DATE_Serializer
    default_t = 'D_DATE'

class API_Datawarehouse_D_LOCATION(BaseAPI):
    """API for D_LOCATION model."""
    model_D_LOCATION = D_LOCATION
    serializer_D_LOCATION = D_LOCATION_Serializer
    default_t = 'D_LOCATION'

class API_Datawarehouse_F_FLUX(BaseAPI):
    """API for F_FLUX model."""
    model_F_FLUX = F_FLUX
    serializer_F_FLUX = F_FLUX_Serializer
    default_t = 'F_FLUX'
