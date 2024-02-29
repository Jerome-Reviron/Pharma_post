from rest_framework import serializers
from app.models import Flux
from app.models import D_TYPE_VACCIN, D_DATE, D_LOCATION
from app.models import F_FLUX

class Flux_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Flux
        fields = '__all__'

class D_TYPE_VACCIN_Serializer(serializers.ModelSerializer):
    class Meta:
        model = D_TYPE_VACCIN
        fields = '__all__'

class D_DATE_Serializer(serializers.ModelSerializer):
    class Meta:
        model = D_DATE
        fields = '__all__'

class D_LOCATION_Serializer(serializers.ModelSerializer):
    class Meta:
        model = D_LOCATION
        fields = '__all__'

class F_FLUX_Serializer(serializers.ModelSerializer):
    class Meta:
        model = F_FLUX
        fields = '__all__'
