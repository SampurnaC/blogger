from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=10)
    description = models.TextField(max_length=100)

    def __str__(self):
        return self.title

class Comment(models.Model):
    blog = models.ForeignKey(Blog, related_name="comments", on_delete=models.CASCADE)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.blog.title
