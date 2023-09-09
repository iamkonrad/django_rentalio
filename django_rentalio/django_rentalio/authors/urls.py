from django.urls import path

from authors.views import AuthorsListView, AuthorDetailView

app_name='authors'

urlpatterns = [

    path('', AuthorsListView.as_view(), {'letter': None}, name='main'),
    path('<str:letter>/', AuthorsListView.as_view(), name='main'),
    path('details/<str:name>/', AuthorDetailView.as_view(), name='details'),

]
