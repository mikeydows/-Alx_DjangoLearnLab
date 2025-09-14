from django.contrib import admin
from .models import Author, Library, Librarian, Book, UserProfile
# Register your models here.

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)     
admin.site.register(Librarian)
admin.site.register(UserProfile)