"""
URL configuration for portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('admindashboard/', admin.site.urls),
    path('', views.index, name='index'),
    path('about_me/', views.about_me, name='about_me'),
    path('projects/', views.projects, name='projects'),
    path('articles/', views.all_articles, name='articles'),
    path('articles/<slug:slug>/', views.article, name='article'),
]

handler404 = 'app.views.page_not_found'
handler500 = 'app.views.server_error'
