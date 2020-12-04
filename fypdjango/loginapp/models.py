from django.db import models

#from django.contrib.auth.models import User
from django.utils import timezone

from django.conf import settings
# Create your models here.
#everytime we create a model django create 4 different permissions

class usersAuthentication(models.Model):
    name = models.CharField(max_length=120)
    username = models.CharField(max_length=120)
    department = models.CharField(max_length=120)
    password = models.CharField(max_length=120)

    def __str__(self):
        return self.username





class Post(models.Model):

    class PostObjects(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status='published')#space before filter

    options = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    title = models.CharField(max_length=250)
    description = models.TextField(null=True)#description
    content = models.TextField()#upload files here later
    slug = models.SlugField(max_length=250, unique_for_date='published')#used to store url
    published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='posts')#changed from blog_posts
    status = models.CharField(
        max_length=10, choices=options, default='published')

    objects = models.Manager()  # default manager
    postobjects = PostObjects()  #filtering all the objects in a database that are published

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title
