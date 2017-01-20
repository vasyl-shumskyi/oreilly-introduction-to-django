from django.db.models import Count
from django.shortcuts import render
from django.views.generic import View
from books.models import Author, Book


def list_books(request):
    '''
    List the books that have reviews
    '''

    books = Book.objects.exclude(date_reviewed__isnull=True).prefetch_related('authors')

    context = {
        'books': books,
        }

    return render(request, "list.html",context)

class AuthorList(View):
    def get(self, request):

        #authors = Author.objects.all()

        authors = Author.objects.annotate(
            published_books = Count('books')
        ).filter(
            published_books__gt=0
        )

        context = {
            'authors': authors
        }

        return render(request, "authors.html", context)