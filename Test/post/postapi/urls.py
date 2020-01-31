from django.urls import path
from .views import PostListCreateView, PostRetriveUpdateDistroyView
urlpatterns= [
    path('post-api/', PostListCreateView.as_view()),
    path('post-api/<int:id>/',PostRetriveUpdateDistroyView.as_view()),

]