from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('books', views.books),
    path('add_book', views.add_book),
    path('render_books', views.render_books),
    path('books/<int:book_id>', views.update_book),
]