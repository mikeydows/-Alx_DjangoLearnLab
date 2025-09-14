from django.shortcuts import render, get_object_or_404, redirect
# from django.views.generic import DetailView
from .models import Library, Book, Author
# from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm # A built-in form for creating new users.
from django.shortcuts import render # Used to return an HTML response with a template.
from django.contrib.auth.decorators import user_passes_test # A decorator that restricts access to views based on a custom test function.
from django.contrib.auth.decorators import permission_required # A decorator that restricts access to views based on user permissions.
from django.contrib import messages
from .forms import BookForm

# Create your views here.

# Function-based View to display list of books
@permission_required('relationship_app.can_view', raise_exception=True)
def list_books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)

# Class-based view that displays details for a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
    
    def dispatch(self, request, *args, **kwargs):
        # Check if user has view permission before displaying library details
        if not request.user.has_perm('relationship_app.can_view'):
            from django.http import HttpResponseForbidden
            return HttpResponseForbidden("You don't have permission to view this content.")
        return super().dispatch(request, *args, **kwargs)

# Register view
class RegisterView(CreateView):
    form_class = UserCreationForm
    # If this is a function based view it would be 
    # form = UserCreationForm()
    success_url = reverse_lazy('login')
    template_name = 'relationship_app/register.html'


# Role-checking functions
def is_admin(user):
    return user.is_authenticated and user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.is_authenticated and user.userprofile.role == 'Librarian'

def is_member(user):
    return user.is_authenticated and user.userprofile.role == 'Member'

# Role protected views using user_passes_test decorator
# Admin
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

# Librarian
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

# Member
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')


# Permission-based views
@permission_required('relationship_app.can_create', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book created successfully!')
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'relationship_app/book_form.html', {'form': form, 'action': 'Add'})

@permission_required('relationship_app.can_edit', raise_exception=True)
def change_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book updated successfully!')
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'relationship_app/book_form.html', {'form': form, 'action': 'Edit'})

@permission_required('relationship_app.can_delete', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        messages.success(request, 'Book deleted successfully!')
        return redirect('book_list')
    return render(request, 'relationship_app/book_confirm_delete.html', {'book': book})