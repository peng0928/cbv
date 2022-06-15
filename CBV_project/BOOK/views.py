from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
# FBV
# @csrf_exempt
# def book(request):
#     if request.method == 'GET':
#         return HttpResponse('Get')
#
#     else:
#         return HttpResponse('Post')
from django.views import View
from rest_framework.views import APIView

class BookView(APIView):

    def get(self, request):
        return HttpResponse('Get')

    def post(self, request):
        print(request.data)
        return HttpResponse('POST')

    def delete(self, request):
        return HttpResponse('del')
