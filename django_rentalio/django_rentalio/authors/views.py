from django.shortcuts import get_object_or_404
import string
from django.views.generic import ListView, DetailView, FormView
from .forms import AuthorForm
from books.models import BookTitle, Book
from authors.models import Author
from urllib.parse import unquote
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin




class AuthorsListView(LoginRequiredMixin, FormView, ListView):
    model = Author
    template_name = 'authors/main.html'
    form_class = AuthorForm
    i_instance = None

    def get_queryset(self):
        parameter = self.kwargs.get('letter') or 'A'
        if parameter == "all":
            return Author.objects.all().order_by('name')
        elif parameter.isdigit():
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

    def form_valid(self, form):
        self.i_instance = form.save()
        messages.add_message(self.request, messages.INFO, f"Author: {self.i_instance.name} has been added to the db.")
        return super().form_valid(form)

    def form_invalid(self, form):
        self.object_list = self.get_queryset()
        messages.add_message(self.request, messages.ERROR, form.errors)
        return super().form_invalid(form)

    def get_success_url(self):
        return self.request.path

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
