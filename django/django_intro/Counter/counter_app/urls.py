from django.urls import path     
from . import views
urlpatterns = [
    path('', views.index),
    path('destroy_session',views.delete),	   
    path('destroy_session/',views.delete),	   
]