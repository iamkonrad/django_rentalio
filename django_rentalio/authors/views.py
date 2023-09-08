from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import FormView, ListView

from authors.models import Author


# Create your views here.



class AuthorsListView(LoginRequiredMixin, ListView):
    model = Author
    template_name = 'authors/main.html'



