# Query all books by a specific author.
from os import name
from relationship_app.models import Book, Author, Library

# author_books = Book.objects.filter(author="author_name")
# Author.objects.get(name=author_name)", "objects.filter(author=author)


# List all books in a library.
# library_books = Library.objects.get(name="library_name").books.all()
# Library.objects.get(name=library_name).books.all()



# Retrieve the librarian for a library.
# librarian = Library.objects.get(name="library_name").librarian
# Librarian.objects.get(library=