from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from django.conf import UserSettingsHolder, settings
from .models import Post, Tag, Dsuser

# Create your models here.

class Dsuser(AbstractUser):
    email = models.EmailField(max_length=128)
    password = models.CharField(max_length=128)
    register_date = models.DateField(auto_now_add=True)
    
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    imgsrc = models.CharField(max_length=1024)
    contents = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    tag = models.ManyToManyField(Tag, on_delete=models.RESTRICT)

    def publish(self):
        self.save()

    def __str__(self):
        return self.contents

class Tag(models.Model):
    tagname = models.CharField(max_length=128)
    posts = models.ManyToManyField(Post)