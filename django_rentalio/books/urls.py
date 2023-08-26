from django.urls import path
from .views import BookTitleListView, BookTitleDetailView,BookDetailView


app_name='books'

urlpatterns = [


    path('', BookTitleListView.as_view(), {'letter':None},name='main'),
    path('<str:letter>/', BookTitleListView.as_view(), name='main'),
    path('<str:letter>/<slug>/',BookTitleDetailView.as_view(),name='detail'),
    path('<str:letter>/<slug>/<str:isbn>/', BookDetailView.as_view(), name='detail-book'),

]

