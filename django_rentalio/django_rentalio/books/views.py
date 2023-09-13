from django.shortcuts import get_object_or_404
from .models import BookTitle, Book
from django.views.generic import ListView, FormView, DetailView, DeleteView
from .forms import BookTitleForm
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


class BookDetailView(LoginRequiredMixin,DetailView):
    model=Book
    template_name = 'books/detail_book.html'

    def get_object(self):
        id = self.kwargs.get('book_id')
        obj=get_object_or_404(Book,id=id)
        return obj

class BookDeleteView(LoginRequiredMixin,DeleteView):
    model=Book
    template_name = 'books/confirm_delete.html'

    def get_object(self):
        id = self.kwargs.get('book_id')
        obj = get_object_or_404(Book, ISBN=id)
        return obj

    def get_success_url(self):
        messages.add_message(self.request,messages.INFO,f"The book with isbn{self.get_object().ISBN} has been removed.")
        letter=self.kwargs.get('letter')
        slug=self.kwargs.get('slug')
        return reverse('books:detail',kwargs={'letter':letter,'slug':slug})
