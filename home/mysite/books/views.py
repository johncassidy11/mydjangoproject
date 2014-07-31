# Create your views here.
from django.shortcuts import render_to_response
from books.models import Book


def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('vvedite poiskovoi zapros')
        elif len(q) > 20:
            errors.append('ne bolee 20 simvolov')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_results.html',
                                      {'books':books,'query':q })
    return render_to_response('search_form.html',{'errors':errors})
