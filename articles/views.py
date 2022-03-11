from django.views import generic

from services.articleService import aggreate_by_genre_field
from .models import Article


# Create your views here.
class ArticleDetailView(generic.DetailView):
    model = Article
    queryset = Article.objects.exclude(published=None).select_related('genre', 'author')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ArticleDetailView, self).get_context_data()
        context['totals'] = aggreate_by_genre_field(self.queryset)
        return context


class ArticleListView(generic.ListView):
    model = Article
    queryset = Article.objects.exclude(published=None).select_related('genre', 'author')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ArticleListView, self).get_context_data()
        context['totals'] = aggreate_by_genre_field(self.queryset)
        return context


class ArticleWeekView(generic.WeekArchiveView):
    model = Article
    date_field = 'published'
    allow_future = False
    make_object_list = True
    queryset = Article.objects.exclude(published=None).select_related('genre', 'author')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ArticleWeekView, self).get_context_data()
        context['totals'] = aggreate_by_genre_field(self.queryset)
        return context


class ArticleMonthView(generic.MonthArchiveView):
    model = Article
    date_field = 'published'
    allow_future = False
    make_object_list = True
    month_format = '%m'
    queryset = Article.objects.exclude(published=None).select_related('genre', 'author')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ArticleMonthView, self).get_context_data()
        context['totals'] = aggreate_by_genre_field(self.queryset)
        return context


class ArticleYearView(generic.YearArchiveView):
    model = Article
    date_field = 'published'
    allow_future = False
    make_object_list = True
    queryset = Article.objects.exclude(published=None).select_related('genre', 'author')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ArticleYearView, self).get_context_data()
        context['totals'] = aggreate_by_genre_field(self.queryset)
        return context
