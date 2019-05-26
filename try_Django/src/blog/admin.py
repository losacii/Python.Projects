from django.contrib import admin
from .models import Post
# Register your models here.

# Register 'Post' to admin-page
# in blog/admin.py, import Post, then register it.
admin.site.register(Post)





