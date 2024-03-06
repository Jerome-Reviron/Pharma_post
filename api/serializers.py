from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

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

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        if not username or not password:
            raise serializers.ValidationError("Username and password are required.")

        user = authenticate(request=self.context.get('request'), username=username, password=password)

        if not user or not user.is_active:
            raise serializers.ValidationError("Invalid username or password")

        data['user'] = user
        return data