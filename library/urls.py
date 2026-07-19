from django.urls import path
from .views import BookView, BookDetail

urlpatterns=[
    path("books/",BookView.as_view()),
    path("books/<int:book_id>/",BookDetail.as_view())
]