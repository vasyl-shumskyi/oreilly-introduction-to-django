#from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from books.models import Book


def list_books(request):
    '''
    List the books that have reviews
    '''

    books = Book.objects.exclude(date_reviewed__isnull=True).prefetch_related('authors')

    context = {
        'books': books,
        }

#   return HttpResponse("We could put anything here")
#   return HttpResponse(request.user.username)
    return render(request, "list.html",context)