from django.http import HttpResponseRedirect, JsonResponse
from customers.models import Customer
from books.models import Book, BookTitle
from django.views.generic import TemplateView
from django.db.models import Count
from rentals.models import Rental
from publishers.models import Publisher
from rentals.choices import STATUS_CHOICES
from .forms import LoginForm,OTPForm
from django.contrib.auth import login,authenticate, logout
from django.contrib import messages
from django.shortcuts import render
from .utils import send_otp


def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method=='POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request,username=username,password=password)
            if user is not None:
                send_otp(request)
            else:
                messages.add_message(request,messages.ERROR, 'Invalid username or password')
    context = {
        'form':form
    }

    return render(request,'login.html',context)

class DashboardView(TemplateView):
    template_name='dashboard.html'

def chart_data(request):
    data = []


    all_books = len(Book.objects.all())
    all_book_titles = len(BookTitle.objects.all())
    data.append({
        'labels': ['books', 'book titles'],
        'data': [all_books, all_book_titles],
        'description': 'unique book titles vs books',
        'type': 'bar',
    })

    titles_by_publisher = BookTitle.objects.values('publisher__name').annotate(Count('publisher__name'))
    publisher_names=[x['publisher__name'] for x in titles_by_publisher]
    publisher_names_count=[x['publisher__name__count'] for x in titles_by_publisher]
    data.append({
        'labels':publisher_names,
        'data':publisher_names_count,
        'description':'book title count by publisher',
        'type':'pie',
    })

    book_by_status = Rental.objects.values('status').annotate(Count('book__title'))
    book_title_count = [x['book__title__count'] for x in book_by_status]
    status_keys = [x['status'] for x in book_by_status]
    status = [dict(STATUS_CHOICES)[key] for key in status_keys]
    data.append({
        'labels':status,
        'data':book_title_count,
        'description':'book by status',
        'type':'pie',
    })

    customers = len(Customer.objects.all())
    publishers = len(Publisher.objects.all())
    data.append({
        'labels':['customers','publishers'],
        'data':[customers,publishers],
        'description': 'customers vs publishers',
        'type':'bar',
    })

    return JsonResponse ({'data': data})
def change_theme(request):
    if 'is_dark_mode' in request.session:
        request.session['is_dark_mode'] = not request.session['is_dark_mode']
    else:
        request.session['is_dark_mode'] = True
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

