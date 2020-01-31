from django.urls import path
from .views import PostCreateView,PostDeleteView,PostDetailView,PostListView,PostUpdateView
urlpatterns = [
    path('home/',PostListView.as_view(),name='home'),
    path('<int:pk>/',PostDetailView.as_view(),name='post-detail'),
    path('postcreate/',PostCreateView.as_view(),name='post-create'),
    path('postupdate/<int:pk>/',PostUpdateView.as_view(),name='post-update'),
    path('postdelete/<int:pk>/',PostDeleteView.as_view(),name = 'post-delete'),
]