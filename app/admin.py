from django.contrib import admin
from .models import Project, Tag, Article


admin.site.register(Project)
admin.site.register(Tag)
admin.site.register(Article)
