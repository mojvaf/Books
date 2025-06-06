from django.views.generic import TemplateView
from django.views.generic import ListView, DetailView
from .models.authors import Author
from .models.posts import Post


class TeamPage(TemplateView):
    template_name = "team.html"


class ProjectsPage(TemplateView):
    template_name = "projects.html"


class PapersPage(TemplateView):
    template_name = "papers.html"


# DataBase


class AuthorsListView(ListView):
    model = Author
    context_object_name = "list_authors"
    template_name = "authors.html"


class PostListView(ListView):
    model = Post
    template_name = "posts.html"


class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"
    template_name = "post_detail.html"
