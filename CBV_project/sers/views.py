from django.shortcuts import *

# Create your views here.
from rest_framework.views import APIView
from rest_framework import serializers
from rest_framework.response import Response
from .models import Book,Publish,Author

# 1 基于APIviews的接口实现

# class BookSerializers(serializers.Serializer):
#     title = serializers.CharField(max_length=32)
#     price = serializers.IntegerField()
#     date = serializers.DateField(source='pub_date')
#
#     def create(self, validated_data):
#         new_book = Book.objects.create(**self.validated_data)
#         return new_book
#
#     def update(self, instance, validated_data):
#         new_book = Book.objects.filter(pk=instance.id).update(**validated_data)
#         updated_book = Book.objects.get(pk=instance.id)
#         return updated_book

# class BookSerializers(serializers.ModelSerializer):
#     date = serializers.DateField(source='pub_date')
#     class Meta:
#         model = Book
#         # fields = '__all__'
#         exclude = ['pub_date']
#
#
# class BookViews(APIView):
#
#     def get(self, request):
#         book_list = Book.objects.all()
#
#         serializer = BookSerializers(instance=book_list, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#
#         serializer = BookSerializers(data=request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)
#
#
# class BookDetail(APIView):
#     def get(self, request, id):
#         book_list = Book.objects.get(pk=id)
#
#         serializer = BookSerializers(instance=book_list)
#         return Response(serializer.data)
#
#     def delete(self, request, id):
#         Book.objects.get(pk=id).delete()
#         return Response(f'已删除--{id}')
#
#
#     def put(self, request, id):
#         update_book = Book.objects.get(pk=id)
#         serializer = BookSerializers(instance=update_book, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return  Response(serializer.data)
#         else:
#             return Response(serializer.errors)


# 2 基于GenericAPIviews接口实现
from rest_framework.generics import GenericAPIView
class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class PulishSerializers(serializers.ModelSerializer):
    class Meta:
        model = Publish
        fields = '__all__'



class BookViews(GenericAPIView):

    def get(self, request):
        book_list = Book.objects.all()

        serializer = BookSerializers(instance=book_list, many=True)
        return Response(serializer.data)

    def post(self, request):

        serializer = BookSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class PulishViews(GenericAPIView):
    queryset = Publish.objects.all()
    serializer_class = PulishSerializers

    def get(self, request):
        serializer = self.get_serializer(instance=self.get_queryset(), many=True)
        return Response(serializer.data)

    def post(self, request):

        serializer = PulishSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        else:
            return Response(serializer.errors)



















