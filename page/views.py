from django.views.generic import TemplateView

class TeamPage(TemplateView):
    template_name = 'team.html'
    
class ProjectsPage(TemplateView):
    template_name = 'projects.html' 


class PapersPage(TemplateView):
    template_name = 'papers.html'       
