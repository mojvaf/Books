"""xproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from page.views import TeamPage
from page.views import ProjectsPage
from page.views import PapersPage
from page.views import AuthorsListView
from page.views import PostListView, PostDetailView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("team/", TeamPage.as_view(), name="team"),
    path("projects/", ProjectsPage.as_view(), name="projects"),
    path("papers/", PapersPage.as_view(), name="papers"),
    path("authors/", AuthorsListView.as_view(), name="authors"),
    path("post-list/", PostListView.as_view(), name="post-list"),
    path("post-detail/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
