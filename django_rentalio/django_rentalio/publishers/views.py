from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView, FormView
from books.models import BookTitle, Book
from publishers.models import Publisher
import string
from urllib.parse import unquote
from .forms import PublisherForm
from django.contrib import messages




class PublishersListView(LoginRequiredMixin, FormView,ListView):
    template_name = 'publishers/main.html'
    form_class = PublisherForm
    i_instance = None

    def get_queryset(self):
        parameter = self.kwargs.get('letter') or 'A'
        if parameter == "all":
            return Publisher.objects.all().order_by('name')
        elif parameter.isdigit():
            return Publisher.objects.filter(name__startswith=parameter)
        else:
            return Publisher.objects.filter(name__istartswith=parameter)

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
        messages.add_message(self.request, messages.INFO, f"Publisher: {self.i_instance.name} has been added.")
        return super().form_valid(form)

    def form_invalid(self, form):
        self.object_list = self.get_queryset()
        messages.add_message(self.request, messages.ERROR, form.errors)
        return super().form_invalid(form)

    def get_success_url(self):
        return self.request.path

class PublishersDetailView(LoginRequiredMixin,DetailView):
    model = Publisher
    template_name = 'publishers/detail.html'

    def get_object(self,queryset=None):
        name=self.kwargs.get('name')
        name=unquote(name)
        return get_object_or_404(Publisher,name=name)

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['book_titles']=BookTitle.objects.filter(publisher=self.object)
        context['books'] = Book.objects.filter(title__publisher=self.object)
        return context
