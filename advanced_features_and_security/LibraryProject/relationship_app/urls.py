from django.urls import path
from .views import list_books, LibraryDetailView, RegisterView, admin_view, librarian_view, member_view, add_book, change_book, delete_book
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [

    # Book and Library Urls
    path('books/', list_books, name='book_list'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Authentication Urls
    path('register/', RegisterView.as_view(), name='register'),
    # path('register/', views.register, name='register'), Function based view alternative
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    # Role-based Urls
    path('admin-view/', admin_view, name='admin_view'),
    path('librarian-view/', librarian_view, name='librarian_view'),
    path('member-view/', member_view, name='member_view'),

    # Permission based Urls
    path('add_book/', add_book, name='add_book'),
    path('edit_book/<int:pk>/', change_book, name='change_book'),
    path('delete_book/<int:pk>/', delete_book, name='delete_book')

]
