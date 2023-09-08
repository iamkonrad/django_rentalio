from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
import string
from django.views.generic import FormView, ListView, DetailView
from books.models import BookTitle
from authors.models import Author


# Create your views here.


class AuthorsListView(LoginRequiredMixin, ListView):
    model = Author
    template_name = 'authors/main.html'

    def get_queryset(self):
        parameter = self.kwargs.get('letter') or 'A'
        if parameter.isdigit():
            return Author.objects.filter(name__startswith=parameter)
        else:
            return Author.objects.filter(name__istartswith=parameter)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        letters = list(string.ascii_uppercase)
        numbers = [str(i) for i in range(10)]

        context['letters'] = letters
        context['numbers'] = numbers
        context['selected_letter'] = self.kwargs.get('letter') or 'A'
        return context


class AuthorDetailView(LoginRequiredMixin,DetailView):
    model = BookTitle
    template_name = 'authors/details.html'
