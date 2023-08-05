from typing import Any, List
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, render
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


# TODO: Convert this into class-based view
def post_single(request, post):
    post = get_object_or_404(Post, slug=post, status="published")
    related = Post.objects.filter(author=post.author)[:5]
    return render(request, "blog/single.html", {"post": post, "related": related})


class TagListView(ListView):
    model = Post
    paginate_by = 10
    context_object_name = "posts"

    def get_queryset(self):
        x = Post.objects.filter(tags__name__in=[self.kwargs["tag"]])
        print(x)

        return x

    def get_template_names(self):
        return "blog/tags.html"
