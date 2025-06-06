from django.contrib import admin
from .models.authors import Author
from .models.posts import Post

admin.site.register(Author)
admin.site.register(Post)
