from django.views.generic import View, DetailView
from django.db.models import Count
from django.shortcuts import render
from .models import Book, Author


# Create your views here.


def list_books(request):
    """
    List all books
    :param request:
    :return:
    """
    books = Book.objects.exclude(date_reviewed__isnull=True).prefetch_related('authors')
    context = {
        'books': books
    }

    return render(request, "list.html", context)


class AuthorList(View):
    def get(self, request):
        authors = Author.objects.annotate(published_books=Count('books')).filter(published_books__gt=0)
        context = {
            'authors': authors
        }

        return render(request, "authors.html", context)


class AuthorDetail(DetailView):
    model = Author
    template_name = 'author.html'


class BookDetail(DetailView):
    model = Book
    template_name = 'book.html'
