from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField(max_length=1000)

    def __str__(self):
        return f" Post by | {self.author}"

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})
