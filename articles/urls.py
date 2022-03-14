from django.urls import include, path
from articles import views

urlpatterns = [
    path('<int:year>/', views.ArticleYearView.as_view()),
    path('<int:year>/<int:month>/', views.ArticleMonthView.as_view()),
    path('', views.ArticleListView.as_view()),
    path('<pk>', views.ArticleDetailView.as_view()),
]
