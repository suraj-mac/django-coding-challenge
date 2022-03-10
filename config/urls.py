"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include

from articles import views
from authors import views as author_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('articles/<int:year>/', views.ArticleYearView.as_view()),
    path('articles/<int:year>/<int:month>/', views.ArticleMonthView.as_view()),
    path('articles/', views.ArticleListView.as_view()),
    path('articles/<pk>', views.ArticleDetailView.as_view()),
    path('authors/<pk>', author_views.AuthorsDetailView.as_view(), name='author-detail'),




    path('__debug__/', include('debug_toolbar.urls')),
]
