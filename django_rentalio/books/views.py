from django.shortcuts import render
from .models import BookTitle
from django.views.generic import ListView

#def book_title_list_view(request):
#    qs=BookTitle.objects.all()
#    return render(request, 'books/main.html',{'qs':qs})

class BookTitleListView(ListView):
    queryset=BookTitle.objects.all()
    model = BookTitle
    template_name='books/main.html'

    def get_queryset(self):
        parameter="a"
        return BookTitle.objects.filter(title__startswith=parameter)

def book_title_detail_view(request,**kwargs):
    pk=kwargs.get('pk')
    obj=BookTitle.objects.get(pk=pk)
    return render(request,'books/detail.html',{'obj':obj})
