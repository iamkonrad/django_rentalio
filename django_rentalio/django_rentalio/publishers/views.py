from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import FormView, ListView

from publishers.models import Publisher
import string



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
