from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('addBook',views.addBook),
    path('shows/<int:id>',views.welcome),
    path('shows')
]


# every form should have 1.Rout for Render 2.Rout for Handel the Data 