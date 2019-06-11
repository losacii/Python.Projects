# blog/models.py
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.db.models import Q

User = settings.AUTH_USER_MODEL

class PostQuerySet(models.QuerySet):
    def published(self):
        now = timezone.now()
        return self.filter(publish_date__lte=now)

    def search(self, query):
        lookup = (
            Q(title__icontains=query) |
            Q(slug__icontains=query) |
            Q(content__icontains=query)
        )
        return self.filter(lookup)

class PostManager(models.Manager):
    def get_queryset(self):
        return PostQuerySet(self.model, using=self._db)
    
    def published(self):
        return self.get_queryset().published()

    def search(self, query=None):
        if query:
            return self.get_queryset().published().search(query)
        else:
            return self.get_queryset().none()

class Post(models.Model):
    title = models.CharField(max_length=99)
    image = models.ImageField(upload_to='image/', blank=True, null=True)
    slug = models.SlugField(unique=True)
    content = models.TextField(null=True, blank=True)

    user = models.ForeignKey(User, default=1, null=True, on_delete=models.SET_NULL)
    # default=1 ~ if a new post, user set to first user

    publish_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now=True)

    objects = PostManager()

    class Meta:
        ordering = ['-updated', '-publish_date', 'timestamp', 'pk']

    def __str__(self):
        return f"({self.id}){self.title}"

    def get_url(self):
        return f"/blog/{self.slug}"

    def edit_url(self):
        return f"/blog/{self.slug}/update"

    def delete_url(self):
        return f"{self.get_url()}/delete"
