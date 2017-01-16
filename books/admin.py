from django.contrib import admin

# Register your models here.
from books.models import Book

admin.site.register(Book)
