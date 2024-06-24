from django.urls import path

from libraryManagement import views

urlpatterns = [
    path('view_all', views.view_all_books),
    path("borrow_book", views.borrow_book),
    path("signup", views.signup),
    path("login", views.login),
]