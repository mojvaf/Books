from django.db import models


class Authors(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    bio = models.TextField(blank=True, null=True)
    create_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
