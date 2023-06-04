import os, django, random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blogger.settings")
django.setup()

from faker import Faker
from blog.models import Blog
from django.contrib.auth.models import User


def create_post(n):
    fake = Faker()
    user = User.objects.get(id=2)

    for i in range(3):
        id = random.randint(1,4)
        title = fake.name()
        description = fake.text()
        created_by=user
        new_blog = Blog(title=title, description=description,created_by=created_by)
        new_blog.save()
    
    user = User.objects.get(id=4)

    for i in range(5):
        id = random.randint(1,4)
        title = fake.name()
        description = fake.text()
        created_by=user
        new_blog = Blog(title=title, description=description,created_by=created_by)
        new_blog.save()
    
    user = User.objects.get(id=2)

    for i in range(2):
        id = random.randint(1,4)
        title = fake.name()
        description = fake.text()
        created_by=user
        new_blog = Blog(title=title, description=description,created_by=created_by)
        new_blog.save()
create_post(10)
