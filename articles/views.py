from django.views import generic
from .models import Article


# Create your views here.
class ArticleDetailView(generic.DetailView):
    model = Article

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ArticleDetailView, self).get_context_data()
        totals = dict()
        query_set = Article.objects.exclude(published=None).select_related('genre', 'author')
        for article in query_set:
            if article.genre in totals.keys():
                totals[article.genre] += 1
            else:
                totals[article.genre] = 1

        context['totals'] = totals

        return context


class ArticleListView(generic.ListView):
    model = Article
    queryset = Article.objects.exclude(published=None).select_related('genre', 'author')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ArticleListView, self).get_context_data()
        totals = dict()

        for article in self.queryset:
            if article.genre in totals.keys():
                totals[article.genre] += 1
            else:
                totals[article.genre] = 1

        context['totals'] = totals

        return context


class ArticleWeekView(generic.WeekArchiveView):
    model = Article
    date_field = 'published'
    allow_future = False
    make_object_list = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ArticleWeekView, self).get_context_data()

        totals = dict()
        query_set = Article.objects.exclude(published=None).select_related('genre', 'author')
        for article in query_set:
            if article.genre in totals.keys():
                totals[article.genre] += 1
            else:
                totals[article.genre] = 1

        context['totals'] = totals

        return context


class ArticleMonthView(generic.MonthArchiveView):
    model = Article
    date_field = 'published'
    allow_future = False
    make_object_list = True
    month_format = '%m'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ArticleMonthView, self).get_context_data()
        totals = dict()
        query_set = Article.objects.exclude(published=None).select_related('genre', 'author')
        for article in query_set:
            if article.genre in totals.keys():
                totals[article.genre] += 1
            else:
                totals[article.genre] = 1

        context['totals'] = totals

        return context


class ArticleYearView(generic.YearArchiveView):
    model = Article
    date_field = 'published'
    allow_future = False
    make_object_list = True

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ArticleYearView, self).get_context_data()
        totals = dict()
        query_set = Article.objects.exclude(published=None).select_related('genre', 'author')
        for article in query_set:
            if article.genre in totals.keys():
                totals[article.genre] += 1
            else:
                totals[article.genre] = 1

        context['totals'] = totals

        return context
