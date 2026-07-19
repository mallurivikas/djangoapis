from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Book
from .serializers import BookSerializer

class BookView(APIView):
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