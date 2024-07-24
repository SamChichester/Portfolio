from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.http import Http404
from django.utils.html import escape
import re
from .models import Project, Tag


def index(request):
    return render(request, 'app/index.html', {'title': 'Home'})


def about_me(request):
    return render(request, 'app/about_me.html', {'title': 'About Me'})


def is_valid_tag(tag):
    if tag is None:
        return False
    pattern = re.compile(r'^[a-zA-Z0-9_]+$')
    return pattern.match(tag) is not None


def projects(request):
    tag_filter = request.GET.get('tags')
    selected_tags = []

    if tag_filter:
        for tag in tag_filter.split(','):
            tag = tag.strip()
            if is_valid_tag(tag):
                selected_tags.append(escape(tag))

    all_tags = Tag.objects.all()
    all_tags_names = [tag.name for tag in all_tags]

    projects = Project.objects.all().order_by('-date')
    for tag in selected_tags:
        if tag in all_tags_names:
            projects = projects.filter(tags__name=tag).distinct()

    paginator = Paginator(projects, 4)
    page_number = request.GET.get('page')

    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.get_page(1)
    except EmptyPage:
        page_obj = paginator.get_page(paginator.num_pages)

    context = {
        'projects': page_obj,
        'tags': all_tags,
        'selected_tags': selected_tags,
    }

    return render(request, 'app/projects.html', context)


def page_not_found(request, exception):
    return render(request, 'app/404.html', status=404)


def server_error(request):
    return render(request, 'app/500.html', status=500)
