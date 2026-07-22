from django.urls import path
from .views import BookView, BookDetail, RegistrationView

urlpatterns=[
    path("books/",BookView.as_view()),
    path("books/<int:book_id>/",BookDetail.as_view()),
    path("register/",RegistrationView.as_view()),
]