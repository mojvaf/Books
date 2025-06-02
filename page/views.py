from django.views.generic import TemplateView
from django.views.generic import ListView
from .models import Authors

class TeamPage(TemplateView):
    template_name = 'team.html'
    
class ProjectsPage(TemplateView):
    template_name = 'projects.html' 


class PapersPage(TemplateView):
    template_name = 'papers.html'       

    
######################
 # Data Base 
######################


class AuthorsListView(ListView):
    model = Authors
    context_object_name = 'list_authors'
    template_name = 'authors.html'
    