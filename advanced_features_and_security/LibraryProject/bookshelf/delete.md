<!-- DELETE -->
>>> from bookshelf.models import Book
>>> book = Book.objects.get(title="Nineteen Eighty-Four")
>>> book.delete()
# Confirm deletion
>>> book.delete()
>>> books = Book.objects.all()
>>> print(f"Books in database: {books.count()}")