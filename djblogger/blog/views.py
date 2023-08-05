from django.shortcuts import render
from django.views.generic import ListView
from .models import Post


class HomeView(ListView):
    """
    Homepage view of blog website.
    """

    model = Post
    context_object_name = "posts"
    paginate_by = 10

    def get_template_names(self):
        if self.request.htmx:
            return "blog/components/post-list-elements.html"
        return "blog/index.html"
