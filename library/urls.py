from django.urls import path

from rest_framework_simplejwt.views import (TokenRefreshView)

from .views import BookView, BookDetail, RegistrationView,LoginView

urlpatterns=[
    path("books/",BookView.as_view()),
    path("books/<int:book_id>/",BookDetail.as_view()),
    path("register/",RegistrationView.as_view()),
    path("login/",LoginView.as_view()),
    path("token/refresh",TokenRefreshView.as_view())
]