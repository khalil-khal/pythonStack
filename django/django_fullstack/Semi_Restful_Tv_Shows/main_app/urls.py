from django.urls import path
from . import views


urlpatterns = [
    path ('',views.shows),

    path('/shows',views.shows),

    path('shows/new',views.new),

    path('shows/add/show',views.add_shows),
    
    path('shows/<int:id>',views.view_show),

    path('shows/shows/<int:id>/edit',views.show_edit),

    path('edit',views.edit_show),


    
]
