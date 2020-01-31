from django.shortcuts import render
from .models import Post
# from django.core.urlresolvers import reverse_lazy
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

# Create your views here.
class PostListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = "__all__"

class PostUpdateView(UpdateView):
    model = Post
    fields = ('post_title','post_details')

class PostDeleteView(DeleteView):
    model = Post
    success_url = reverse_lazy('home')
