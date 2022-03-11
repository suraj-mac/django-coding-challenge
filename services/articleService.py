from django.db.models import QuerySet

def aggreate_by_genre_field(query_set: QuerySet) -> {}:
    totals = dict()
    for article in query_set:
        if article.genre in totals.keys():
            totals[article.genre] += 1
        else:
            totals[article.genre] = 1
    return totals
