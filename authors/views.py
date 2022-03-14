from django.views import generic

from services.articleService import aggreate_by_genre_field
from .models import Author
from  articles.models import Article

class AuthorsDetailView(generic.DetailView):
    model = Author

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AuthorsDetailView, self).get_context_data()
        queryset = Article.objects.filter(author_id__exact=self.kwargs['pk']).select_related('genre')
        context['totals'] = aggreate_by_genre_field(queryset)
        return context
