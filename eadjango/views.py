from django.shortcuts import render
from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Post
from .forms import PostForm


class PostListView(ListView):
    model = Post


class PostCreateView(CreateView):
    model = Post
    form_class = PostForm


class PostDetailView(DetailView):
    model = Post


class PostUpdateView(UpdateView):
    model = Post
    form_class = PostForm
