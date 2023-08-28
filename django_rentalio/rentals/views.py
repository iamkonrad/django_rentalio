from django.shortcuts import render, redirect
from .forms import SearchBookForm
from books.models import Book
from django.views.generic import ListView
from. models import Rental

def search_book_view(request):
    form=SearchBookForm(request.POST or None)
    search_query = request.POST.get('search', None)
    book_ex = Book.objects.filter(ISBN=search_query).exists()

    if search_query is not None and book_ex:
        return redirect ('rentals:detail',search_query)
    context = {
        'form':form,
    }
    return render(request,'rentals/main.html', context)

class BookRentalHistoryView(ListView):
    model = Rental
    template_name='rentals/detail.html'
