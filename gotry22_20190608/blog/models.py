# blog/models.py
from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Post(models.Model):
    title = models.CharField(max_length=99)
    slug = models.SlugField(unique=True)
    content = models.TextField(null=True, blank=True)

    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    # default=1 ~ if a new post, user set to first user

    def __str__(self):
        return f"({self.id}){self.title}"

    def get_url(self):
        return f"/blog/{self.slug}"

    def edit_url(self):
        return f"/blog/{self.slug}/update"

    def delete_url(self):
        return f"/blog/{self.slug}/delete"

