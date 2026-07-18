from django.shortcuts import render

from .models import Book
# Create your views here.
class BookList(APIView):
    def get(self,request):
        books=Book.objects.all()
        serializer=BookSerializer(books,many=True)
        return Response(serializer.data)
