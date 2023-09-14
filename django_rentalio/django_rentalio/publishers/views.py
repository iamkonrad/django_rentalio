from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView

from books.models import BookTitle
from publishers.models import Publisher
import string
from urllib.parse import unquote




class PublishersListView(LoginRequiredMixin, ListView):
    template_name = 'publishers/main.html'

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

        return context
