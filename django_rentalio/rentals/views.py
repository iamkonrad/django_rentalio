from django.shortcuts import render

def search_book_view(request):
    context = {}
    return render(request,'rentals/main.html', context)