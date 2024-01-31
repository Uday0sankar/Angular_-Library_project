from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render
from rest_framework import status, mixins, generics, viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from books.models import Book
from books.serializer import Libraryserializer, userserializer


# Create your views here.
#
# class Booklist(APIView):
#     def get(self, request):
#         books = Book.objects.all()
#         l = Libraryserializer(books, many=True)
#         return Response(l.data)
#
#     def post(self, request):
#         l = Libraryserializer(data=request.data)
#         if l.is_valid():
#             l.save()
#             return Response(l.data, status=status.HTTP_201_CREATED)
#         return Response(l.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class Bookdetails(APIView):
#     def get_object(self, pk):
#         try:
#             return Book.objects.get(pk=pk)
#         except:
#             raise Http404
#
#     def get(self, request, pk):
#         libary = self.get_object(pk)
#         l = Libraryserializer(libary)
#         return Response(l.data)
#
#     def put(self, request, pk):
#         libary = self.get_object(pk)
#         l = Libraryserializer(libary, request.data)
#         if l.is_valid():
#             l.save()
#             return Response(l.data, status=status.HTTP_201_CREATED)
#         return Response(l.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         library = self.get_object(pk)
#         library.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
# class Booklist(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Book.objects.all()
#     serializer_class = Libraryserializer
#
#     def get(self, request):
#         return self.list(request)
#
#     def post(self, request):
#         return self.create(request)
#
#
# class Bookdetails(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = Book.objects.all()
#     serializer_class = Libraryserializer
#
#     def get(self, request, pk):
#         return self.retrieve(request)
#
#     def put(self, request, pk):
#         return self.update(request)
#
#     def delete(self, request, pk):
#         return self.destroy(request)

#
# class Booklist(generics.ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = Libraryserializer
#
#
# class Bookdetails(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = Libraryserializer
#
class Booklist(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = Libraryserializer


class Bookdetails(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin,
                  generics.GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = Libraryserializer

    def get(self, request, pk):
        return self.retrieve(request)

    def put(self, request, pk):
        return self.update(request)

    def delete(self, request, pk):
        return self.destroy(request)


class register(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = userserializer


