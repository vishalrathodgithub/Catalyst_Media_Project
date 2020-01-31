from rest_framework import generics
from account.models import User
from .serializers import RegistrationSerializer, LoginSerializer
from rest_framework.permissions import IsAuthenticated

class UserRegistrationApi(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = RegistrationSerializer
    permission_classes = [IsAuthenticated,]

class UserLoginApi(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = LoginSerializer
    permission_classes = [IsAuthenticated,]