from django.views import generic
from .models import Author
from  articles.models import Article


# Create your views here.
class AuthorsDetailView(generic.DetailView):
    model = Author

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AuthorsDetailView, self).get_context_data()

        totals = dict()
        query_set = Article.objects.filter(author_id__exact=self.kwargs['pk']).select_related('genre')
        for article in query_set:
            if article.genre in totals.keys():
                totals[article.genre] += 1
            else:
                totals[article.genre] = 1

        context['totals'] = totals

        return context


# Create your views here.
