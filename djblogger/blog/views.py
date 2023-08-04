from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


class HomeView(ListView):
    """
    Homepage view of blog website.
    """

    model = Post
    template_name = "blog/index.html"
