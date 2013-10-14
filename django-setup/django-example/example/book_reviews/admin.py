from django.contrib import admin
from book_reviews.models import Author, Book, Genre, Review

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Review)