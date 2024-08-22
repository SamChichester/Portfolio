from django.db import models
from django.utils import timezone
from django_quill.fields import QuillField


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    image_url = models.URLField(null=True, blank=True)
    video_url = models.URLField(null=True, blank=True)
    github_url = models.URLField()
    date = models.DateTimeField(default=timezone.now)
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    def sorted_tags(self):
        return self.tags.order_by('name')


class Article(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = QuillField()
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/articles/{self.slug}'
