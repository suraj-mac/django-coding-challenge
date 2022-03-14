from django.urls import include, path
    
from authors import views

urlpatterns = [
    path('<pk>', views.AuthorsDetailView.as_view(), name='author-detail'),
]
