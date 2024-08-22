from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from django.utils.html import escape
import re
from .models import Project, Tag, Article
from datetime import datetime


def index(request):
    return render(request, 'app/index.html', {'title': 'Home'})


def about_me(request):
    start_date = datetime(2018, 8, 1)
    current_date = datetime.now()
    years_since = current_date.year - start_date.year - ((current_date.month, current_date.day)
                                                         < (start_date.month, start_date.day))

    context = {
        'title': 'About Me',
        'years_since': years_since,
    }
    return render(request, 'app/about_me.html', context)


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
        'title': 'Projects',
        'projects': page_obj,
        'tags': all_tags,
        'selected_tags': selected_tags,
    }

    return render(request, 'app/projects.html', context)


def all_articles(request):
    articles = Article.objects.all().order_by('-date')
    paginator = Paginator(articles, 10)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'title': 'Articles',
        'page_obj': page_obj
    }

    return render(request, 'app/all_articles.html', context)


def article(request, slug):
    article = get_object_or_404(Article, slug=slug)

    context = {
        'title': 'Article',
        'article': article
    }

    return render(request, 'app/article.html', context)


def page_not_found(request, exception):
    return render(request, 'app/404.html', status=404)


def server_error(request):
    return render(request, 'app/500.html', status=500)
