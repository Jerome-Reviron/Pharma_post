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
    model_dict = {
        'Flux': Flux,
        'D_TYPE_VACCIN': D_TYPE_VACCIN,
        'D_DATE': D_DATE,
        'D_LOCATION': D_LOCATION,
        'F_FLUX': F_FLUX,
    }

    serializer_dict = {
        'Flux': Flux_Serializer,
        'D_TYPE_VACCIN': D_TYPE_VACCIN_Serializer,
        'D_DATE': D_DATE_Serializer,
        'D_LOCATION': D_LOCATION_Serializer,
        'F_FLUX': F_FLUX_Serializer,
    }

    default_t = 'D_TYPE_VACCIN'

    def get(self, request, *args, **kwargs):
        t = request.GET.get('t', self.default_t)

        model = self.model_dict.get(t)
        if not model:
            return Response(data={'error': f'Model {t} not found.'}, status=status.HTTP_400_BAD_REQUEST)

        data = model.objects.all()
        count = data.count()

        serializer = self.serializer_dict.get(t)
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
    model_Flux = Flux
    serializer_Flux = Flux_Serializer
    default_t = 'Flux'
    lookup_field = 'id'

    def get(self, request, id=None):
        if id is not None:
            data = Flux.objects.filter(id=id)
        else:
            search_param = request.GET.get('t')
            if search_param:
                # Effectuer une recherche précise sur le champ id
                data = Flux.objects.filter(id=search_param)
            else:
                data = Flux.objects.all()

        serializer = Flux_Serializer(data=data, many=True)
        serializer.is_valid()

        result = {
            'count': data.count(),
            'data': serializer.data
        }

        return Response(data=result, status=status.HTTP_200_OK)

    def post(self, request, id=None):
        data = request.data
        serializer = Flux_Serializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id=None):
        try:
            flux = Flux.objects.get(id=id)
        except Flux.DoesNotExist:
            return Response({'error': 'Flux not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = Flux_Serializer(flux, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id=None):
        try:
            flux = Flux.objects.get(id=id)
        except Flux.DoesNotExist:
            return Response({'error': 'Flux not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = Flux_Serializer(flux, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id=None):
        if id is not None:
            data = Flux.objects.filter(id=id)
            if data.exists():
                data.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({"error": "Flux not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            Flux.objects.all().delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

class API_Datawarehouse_D_TYPE_VACCIN(BaseAPI):
    model_D_TYPE_VACCIN = D_TYPE_VACCIN
    serializer_D_TYPE_VACCIN = D_TYPE_VACCIN_Serializer
    default_t = 'D_TYPE_VACCIN'
    lookup_field = 'vaccinlabel'

    def get(self, request, vaccinlabel=None):
        if vaccinlabel is not None:
            data = D_TYPE_VACCIN.objects.filter(vaccinlabel=vaccinlabel)
        else:
            search_param = request.GET.get('t')
            if search_param:
                # Effectuer une recherche précise sur le champ vaccinlabel
                data = D_TYPE_VACCIN.objects.filter(vaccinlabel=search_param)
            else:
                data = D_TYPE_VACCIN.objects.all()

        serializer = D_TYPE_VACCIN_Serializer(data=data, many=True)
        serializer.is_valid()

        result = {
            'count': data.count(),
            'data': serializer.data
        }

        return Response(data=result, status=status.HTTP_200_OK)

    def post(self, request, vaccinlabel=None):
        data = request.data
        serializer = D_TYPE_VACCIN_Serializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, vaccinlabel=None):
        try:
            d_type_vaccin = D_TYPE_VACCIN.objects.get(vaccinlabel=vaccinlabel)
        except D_TYPE_VACCIN.DoesNotExist:
            return Response({'error': 'D_TYPE_VACCIN not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = D_TYPE_VACCIN_Serializer(d_type_vaccin, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, vaccinlabel=None):
        try:
            d_type_vaccin = D_TYPE_VACCIN.objects.get(vaccinlabel=vaccinlabel)
        except D_TYPE_VACCIN.DoesNotExist:
            return Response({'error': 'D_TYPE_VACCIN not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = D_TYPE_VACCIN_Serializer(d_type_vaccin, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, vaccinlabel=None):
        if vaccinlabel is not None:
            data = D_TYPE_VACCIN.objects.filter(vaccinlabel=vaccinlabel)
            if data.exists():
                data.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({"error": "D_TYPE_VACCIN not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            D_TYPE_VACCIN.objects.all().delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

class API_Datawarehouse_D_DATE(BaseAPI):
    model_D_DATE = D_DATE
    serializer_D_DATE = D_DATE_Serializer
    default_t = 'D_DATE'
    lookup_field = 'date_fin_semaine'

    def get(self, request, date_fin_semaine=None):
        if date_fin_semaine is not None:
            data = D_DATE.objects.filter(date_fin_semaine=date_fin_semaine)
        else:
            search_param = request.GET.get('t')
            if search_param:
                # Effectuer une recherche précise sur le champ date_fin_semaine
                data = D_DATE.objects.filter(date_fin_semaine=search_param)
            else:
                data = D_DATE.objects.all()

        serializer = D_DATE_Serializer(data=data, many=True)
        serializer.is_valid()

        result = {
            'count': data.count(),
            'data': serializer.data
        }

        return Response(data=result, status=status.HTTP_200_OK)

    def post(self, request, date_fin_semaine=None):
        data = request.data
        serializer = D_DATE_Serializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, date_fin_semaine=None):
        try:
            d_date = D_DATE.objects.get(date_fin_semaine=date_fin_semaine)
        except D_DATE.DoesNotExist:
            return Response({'error': 'D_DATE not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = D_DATE_Serializer(d_date, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, date_fin_semaine=None):
        try:
            d_date = D_DATE.objects.get(date_fin_semaine=date_fin_semaine)
        except D_DATE.DoesNotExist:
            return Response({'error': 'D_DATE not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = D_DATE_Serializer(d_date, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, date_fin_semaine=None):
        if date_fin_semaine is not None:
            data = D_DATE.objects.filter(date_fin_semaine=date_fin_semaine)
            if data.exists():
                data.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({"error": "D_DATE not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            D_DATE.objects.all().delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

class API_Datawarehouse_D_LOCATION(BaseAPI):
    model_D_LOCATION = D_LOCATION
    serializer_D_LOCATION = D_LOCATION_Serializer
    default_t = 'D_LOCATION'
    lookup_field = 'code_region_code_departement'

    def get(self, request, code_region_code_departement=None):
        if code_region_code_departement is not None:
            data = D_LOCATION.objects.filter(code_region_code_departement=code_region_code_departement)
        else:
            search_param = request.GET.get('t')
            if search_param:
                # Effectuer une recherche précise sur le champ code_region_code_departement
                data = D_LOCATION.objects.filter(code_region_code_departement=search_param)
            else:
                data = D_LOCATION.objects.all()

        serializer = D_LOCATION_Serializer(data=data, many=True)
        serializer.is_valid()

        result = {
            'count': data.count(),
            'data': serializer.data
        }

        return Response(data=result, status=status.HTTP_200_OK)

    def post(self, request, code_region_code_departement=None):
        data = request.data
        serializer = D_LOCATION_Serializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, code_region_code_departement=None):
        try:
            d_location = D_LOCATION.objects.get(code_region_code_departement=code_region_code_departement)
        except D_LOCATION.DoesNotExist:
            return Response({'error': 'D_LOCATION not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = D_LOCATION_Serializer(d_location, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, code_region_code_departement=None):
        try:
            d_location = D_LOCATION.objects.get(code_region_code_departement=code_region_code_departement)
        except D_LOCATION.DoesNotExist:
            return Response({'error': 'D_LOCATION not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = D_LOCATION_Serializer(d_location, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, code_region_code_departement=None):
        if code_region_code_departement is not None:
            data = D_LOCATION.objects.filter(code_region_code_departement=code_region_code_departement)
            if data.exists():
                data.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({"error": "D_LOCATION not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            D_LOCATION.objects.all().delete()
            return Response(status=status.HTTP_204_NO_CONTENT)

class API_Datawarehouse_F_FLUX(BaseAPI):
    model_F_FLUX = F_FLUX
    serializer_F_FLUX = F_FLUX_Serializer
    default_t = 'F_FLUX'
    lookup_field = 'PK_F_FLUX'

    def get(self, request, pk=None):
        if pk is not None:
            data = F_FLUX.objects.filter(PK_F_FLUX=pk)
        else:
            search_param = request.GET.get('t')
            if search_param:
                # Effectuer une recherche précise sur le champ PK_F_FLUX
                data = F_FLUX.objects.filter(PK_F_FLUX=search_param)
            else:
                data = F_FLUX.objects.all()

        serializer = F_FLUX_Serializer(data=data, many=True)
        serializer.is_valid()

        result = {
            'count': data.count(),
            'data': serializer.data
        }

        return Response(data=result, status=status.HTTP_200_OK)

    def post(self, request, pk=None):
        data = request.data
        serializer = F_FLUX_Serializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        try:
            flux = F_FLUX.objects.get(PK_F_FLUX=pk)
        except F_FLUX.DoesNotExist:
            return Response({'error': 'Flux not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = F_FLUX_Serializer(flux, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None):
        try:
            flux = F_FLUX.objects.get(PK_F_FLUX=pk)
        except F_FLUX.DoesNotExist:
            return Response({'error': 'Flux not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = F_FLUX_Serializer(flux, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        if pk is not None:
            data = F_FLUX.objects.filter(PK_F_FLUX=pk)
            if data.exists():
                data.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                return Response({"error": "Flux not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            F_FLUX.objects.all().delete()
            return Response(status=status.HTTP_204_NO_CONTENT)