from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.response import Response
from .models import Accident
from .serializer import *


# Create your views here.
class Index(APIView):
    def get(self, request):
        raw_data = Accident.objects.all()
        serializer = AccidentSerializer(raw_data, many=True)
        return JsonResponse(serializer.data, safe=False)


class IndexPage(APIView):
    def get(self, request, id):
        raw_data = Accident.objects.get(pk=id)
        serializer = AccidentSerializer(raw_data)
        return JsonResponse(serializer.data, safe=False)
