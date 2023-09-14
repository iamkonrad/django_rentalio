from django.urls import path

from .views import PublishersListView, PublishersDetailView



app_name='publishers'

urlpatterns = [

    path('', PublishersListView.as_view(), {'letter': None}, name='main'),
    path('<str:letter>/', PublishersListView.as_view(), name='main'),
    path('details/<str:name>/',PublishersDetailView.as_view(),name='details'),


]
