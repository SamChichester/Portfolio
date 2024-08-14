from django.db import models
from django.utils import timezone


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
