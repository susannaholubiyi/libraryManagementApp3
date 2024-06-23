from django.urls import path

from libraryManagement import views

urlpatterns = [
    path('view_all', views.view_all_books)
]