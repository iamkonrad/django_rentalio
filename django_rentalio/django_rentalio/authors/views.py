from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
import string
from django.views.generic import FormView, ListView, DetailView
from books.models import BookTitle, Book
from authors.models import Author
from urllib.parse import unquote



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
        context['selected_letter'] = self.kwargs.get('letter')
        return context



class AuthorDetailView(LoginRequiredMixin, DetailView):
    model = Author
    template_name = 'authors/details.html'

    def get_object(self, queryset=None):
        name = self.kwargs.get('name')
        name = unquote(name)
        return get_object_or_404(Author, name=name)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['book_titles'] = BookTitle.objects.filter(author=self.object)
        context['books'] = Book.objects.filter(title__author=self.object)
        return context
