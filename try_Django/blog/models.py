from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title



"""
    User.objects.all()  -- querySet
    User.objects.filter(username='vi')  -- querySet

    QuerySet.first()

    user:  id, pk, username

    User.objects.first()  -- user
    User.objects.last()

    dir(User.objects)

    >>> u1 = User.objects.first()
    >>> p = Post()
    >>> p.title="Post One"
    >>> p.content="First Post Content..."
    >>> p.author=u1
    >>> p.save()

    >>> p2 = Post(title='Post Two', content='Secont Post Content! ...', author_id=u1.id)
    >>> p2.save()

    .modeName_set
    >>> u1.post_set.all()
    <QuerySet [<Post: Post One>, <Post: Post Two>]>


"""