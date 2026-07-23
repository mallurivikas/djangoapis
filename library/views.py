from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate


from .models import Book
from .serializers import BookSerializer
from .serializers import RegistrationSerializer

class BookView(APIView):
    permission_classes=[
        IsAuthenticated
    ]
    def get(self,request):
        books=Book.objects.all()
        title=request.query_params.get("title")
        author=request.query_params.get("author")
        price=request.query_params.get("price")
        sort=request.query_params.get("sort")
        if title:
            books=books.filter(
                title__icontains=title
            )
        if author:
            books=books.filter(
                author=author
            )
        if sort:
            books=books.order_by(sort)
        serializer=BookSerializer(books,many=True)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
        
    def post(self,request):
        serializer=BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class BookDetail(APIView):
    def get(self,request,book_id):
        book=get_object_or_404(
            Book,
            id=book_id
        )
        serializer=BookSerializer(book)
        return Response(
            serializer.data,
            status=status.HTTP_200_OK
        )
    def put(self,request,book_id):
        book=get_object_or_404(
            Book,
            id=book_id
        )
        serializer=BookSerializer(
            book,
            data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    def patch(self,request,book_id):
        book=get_object_or_404(
            Book,
            id=book_id
        )
        serializer=BookSerializer(
            book,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    def delete(self,request,book_id):
        book=get_object_or_404(
                Book,
                id=book_id
            )
        book.delete()
        return (
            Response(status.HTTP_204_NO_CONTENT)
        )

class RegistrationView(APIView):
    def post(self,request):
        serializer=RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

class LoginView(APIView):
    def post(self,request):
        username=request.data.get("username")
        password=request.data.get("password")

        user=authenticate(
            username=username,
            password=password
        )
        if user is None:
            return Response(
                {
                    "error":"Invalid Credentials",
                },
                status=status.HTTP_401_UNAUTHORIZED 
            )
        refresh=RefreshToken.for_user(user)
        return Response(
            {
                "refresh":str(refresh),
                "access":str(refresh.access_token)
            },
            status=status.HTTP_200_OK
        )