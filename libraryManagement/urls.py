from django.urls import path

from . import views

urlpatterns = [
    path('view_all/', views.view_all_books),

]