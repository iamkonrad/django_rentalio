from django.shortcuts import get_object_or_404, redirect
from django.views import View

from .forms import BookTitleForm
from .models import BookTitle, Book
from django.views.generic import ListView, FormView, DetailView, DeleteView
from django.urls import reverse
from django.contrib import messages
import string
from django.contrib.auth.mixins import LoginRequiredMixin



class BookTitleListView(LoginRequiredMixin, FormView, ListView):
    template_name = 'books/main.html'
    context_object_name = 'qs'
    form_class = BookTitleForm
    i_instance = None

    def get_success_url(self):
        return self.request.path

    def get_queryset(self):
        parameter = self.kwargs.get('letter') if self.kwargs.get('letter') else 'a'
        if parameter == "all":
            return BookTitle.objects.all().order_by('title')
        elif parameter.isdigit():
            return BookTitle.objects.filter(title__startswith=parameter)
        else:
            return BookTitle.objects.filter(title__istartswith=parameter)

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
        messages.add_message(self.request, messages.INFO, f"Book title: {self.i_instance.title} has been created.")
        return super().form_valid(form)

    def form_invalid(self, form):
        self.object_list = self.get_queryset()
        messages.add_message(self.request, messages.ERROR, form.errors)
        return super().form_invalid(form)

class BookTitleDetailView(LoginRequiredMixin,DetailView):
    model = BookTitle
    template_name = 'books/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['letter'] = self.kwargs.get('letter')
        context['slug'] = self.kwargs.get('slug')
        return context


class BookDetailView(LoginRequiredMixin,DetailView):
    model=Book
    template_name = 'books/detail_book.html'

    def get_object(self, queryset=None):
        if queryset is None:
            queryset = self.get_queryset()

        slug = self.kwargs.get('slug')
        book_id = self.kwargs.get('book_id')
        book_title = get_object_or_404(BookTitle, slug=slug)

        obj = get_object_or_404(Book, id=book_id, title=book_title)

        return obj

class BookDeleteView(LoginRequiredMixin,DeleteView):
    model=Book
    template_name = 'books/confirm_delete.html'

    def get_object(self,queryset=None):
        id = self.kwargs.get('book_id')
        obj = get_object_or_404(Book, id=id)
        return obj

    def get_success_url(self):
        messages.add_message(self.request,messages.INFO,f"The book with id{self.get_object().id} has been removed.")
        return reverse('books:main')


class BookDeleteISBNView(View):
    def post(self, request, *args, **kwargs):
        isbn = self.kwargs.get('ISBN')
        books = Book.objects.filter(ISBN=isbn)                                                                          #filter based on ISBN
        books.delete()
        messages.add_message(request, messages.INFO, f"The books with ISBN {isbn} have been removed.")
        return redirect('books:main')

    def get(self, request, *args, **kwargs):
        return redirect('books:main')
