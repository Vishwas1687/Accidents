from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.response import Response
from .models import Accident
from django.db.models import Q
from .serializer import *
import json


# Create your views here.
class AccidentsView(APIView):
    def get(self, request):
        raw_data = Accident.objects.all()
        serializer = AccidentSerializer(raw_data, many=True)
        return JsonResponse(serializer.data, safe=False)


class AccidentView(APIView):
    def get(self, request, id):
        raw_data = Accident.objects.get(pk=id)
        serializer = AccidentSerializer(raw_data)
        return JsonResponse(serializer.data, safe=False)


class AccidentCategoryView(APIView):
    def get(self, request, category):
        distinct_values = Accident.objects.values_list(category, flat=True).distinct()
        all_accidents = Accident.objects.all()
        result_map = {value: [] for value in distinct_values}
        for acc in all_accidents:
            result_map[getattr(acc, category)].append(
                [acc.latitude, acc.longitude, getattr(acc, category)]
            )
        return JsonResponse({"result_map": result_map}, safe=False)


class AccidentCategoryViewWithCrossFilters(APIView):
    def get(self, request, category):
        filters = request.GET.get("filters", [])
        filters = json.loads(filters)
        final_filter = Q()
        for filter_dict in filters:
            for field_name, field_value in filter_dict.items():
                final_filter &= Q(**{field_name: field_value})
        all_accidents = Accident.objects.filter(final_filter)

        distinct_values = Accident.objects.values_list(category, flat=True).distinct()
        result_map = {value: [] for value in distinct_values}
        for acc in all_accidents:
            result_map[getattr(acc, category)].append(
                [
                    acc.latitude,
                    acc.longitude,
                    getattr(acc, category),
                    acc.weather_condition,
                    acc.month,
                ]
            )
        return JsonResponse({"result_map": result_map}, safe=False)
