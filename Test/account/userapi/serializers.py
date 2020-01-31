from rest_framework import serializers
from account.models import User
class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('Name', 'Password')