from django.db import models
from django.contrib.auth.models import User

from django.utils import timezone
import datetime
class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=700)
    created_date = models.DateTimeField(default=timezone.now)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=True, null=False)
    created_by = models.ForeignKey(User, related_name='blogs', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey(Blog, related_name="comments", on_delete=models.CASCADE, null=True)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.blog.title


