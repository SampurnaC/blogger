import os, django, random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blogger.settings")
django.setup()

from faker import Faker
from blog.models import Blog

def create_post(n):
    fake = Faker()

    for i in range(100):
        id = random.randint(1,4)
        title = fake.name()
        description = fake.text()
        new_blog = Blog(title=title, description=description)
        new_blog.save()
create_post(90)
