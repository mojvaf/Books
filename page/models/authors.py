from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    title = models.CharField(max_length=50, null=True, blank=True)
    bio = models.TextField(blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(default="fallback.png", blank=True)

    def __str__(self):
        return f"Author | {self.first_name} {self.last_name}"
