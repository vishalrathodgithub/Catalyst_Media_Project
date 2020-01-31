from django.urls import path
from .views import UserRegistration,UserLoginView,UserDataView,UserUpdateView,UserDeleteView
urlpatterns = [
    path('userregistration/',UserRegistration.as_view(),name='user-registration'),
    path('userlogin/',UserLoginView.as_view(),name='user-login'),
    path('userdata/',UserDataView.as_view(),name='user-data'),
    path('userupdate/<int:id>/',UserUpdateView.as_view(),name='user-update'),
    path('userdelete/<int:id>/',UserDeleteView.as_view(),name = 'user-delete'),
]