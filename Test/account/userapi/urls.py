from django.urls import path
from .views import UserRegistrationApi, UserLoginApi
urlpatterns= [
    path('user-reg-api/', UserRegistrationApi.as_view()),
    path('user-login-api/',UserLoginApi.as_view()),
]