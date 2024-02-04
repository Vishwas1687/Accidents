from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.response import Response
from .models import Accident
from .utilFunctions import (
    calculate_bounding_box,
)
import pygeohash as geohash
from django.db.models import Count, Sum, Avg
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


class AccidentGroupedByPercentageLocation(APIView):
    def get(self, request, category):
        filtered_accidents = []
        filters = request.GET.get("filters", "[]")
        comparator = request.GET.get("comparator")
        if len(filters) != 0:
            filters = json.loads(filters)
            final_filter = Q()
            for filter_dict in filters:
                for field_name, field_value in filter_dict.items():
                    final_filter &= Q(**{field_name: field_value})
            filtered_accidents = Accident.objects.filter(final_filter)
        else:
            filtered_accidents = Accident.objects.all()

        accidents_grouped_by_geohash = filtered_accidents.values(
            "geo_hash", f"{category}"
        ).annotate(accidents=Count(f"{category}"))
        # Group by geohash and further aggregate by victim_vehicle

        grouped_by_geohash = {}
        geo_hashes = Accident.objects.values_list("geo_hash", flat=True).distinct()
        category_values = Accident.objects.values_list(
            f"{category}", flat=True
        ).distinct()
        for geo_hash in geo_hashes:
            grouped_by_geohash[geo_hash] = {}
            for category_val in category_values:
                grouped_by_geohash[geo_hash][category_val] = 0

        for item in accidents_grouped_by_geohash:
            geo_hash = item["geo_hash"]
            category_val = item[f"{category}"]
            accidents_count = item["accidents"]

            grouped_by_geohash[geo_hash][category_val] += accidents_count

        results = []
        # for geo_hash, category_data in grouped_by_geohash.items():
        #     result = {
        #         "geo_hash": geo_hash,
        #         f"{category}": [
        #             {"type": category, "accidents": count}
        #             for category, count in category_data.items()
        #         ],
        #     }
        #     results.append(result)

        for geo_hash, category_data in grouped_by_geohash.items():
            total_count = 0
            comparator_count = 0
            for category, count in category_data.items():
                if category == comparator:
                    comparator_count = comparator_count + count
                total_count = total_count + count
            percentage_comparison = 0
            if total_count == 0:
                percentage_comparison = 0
            else:
                percentage_comparison = ((comparator_count * 1.0) / total_count) * 100

            result = {
                "geo_hash": geo_hash,
                f"percentage {comparator}": percentage_comparison,
            }
            results.append(result)

        return JsonResponse({"accidents_grouped_by_geohash": results}, safe=False)


class AccidentCategoryPercentageByLocation(APIView):
    def get(self, request, category, category_value):
        filtered_accidents = []
        filters = request.GET.get("filters", "[]")
        if len(filters) != 0:
            filters = json.loads(filters)
            final_filter = Q()
            for filter_dict in filters:
                for field_name, field_value in filter_dict.items():
                    # if (
                    #     isinstance(field_value, dict)
                    #     and "min" in field_value
                    #     and "max" in field_value
                    # ):
                    #     # Handle range query

                    #     final_filter &= Q(**{f"{field_name}__gte": field_value["min"]})
                    #     final_filter &= Q(**{f"{field_name}__lte": field_value["max"]})
                    # else:
                    # Handle regular query
                    final_filter &= Q(**{field_name: field_value})
            filtered_accidents = Accident.objects.filter(final_filter)
        else:
            filtered_accidents = Accident.objects.all()
        category_value_count = filtered_accidents.values(f"{category}").annotate(
            count=Count(f"{category}")
        )
        total_count = 0
        for items in category_value_count:
            category_val = items[f"{category}"]
            count = items["count"]
            if category_val == category_value:
                total_count = count
        accidents_grouped_by_geohash = filtered_accidents.values(
            "geo_hash", f"{category}"
        ).annotate(accidents=Count(f"{category}"))

        grouped_by_geohash = {}
        geo_hashes = Accident.objects.values_list("geo_hash", flat=True).distinct()
        category_values = Accident.objects.values_list(
            f"{category}", flat=True
        ).distinct()
        for geo_hash in geo_hashes:
            grouped_by_geohash[geo_hash] = {}
            for category_val in category_values:
                grouped_by_geohash[geo_hash][category_val] = 0

        for item in accidents_grouped_by_geohash:
            geo_hash = item["geo_hash"]
            category_val = item[f"{category}"]
            accidents_count = item["accidents"]

            grouped_by_geohash[geo_hash][category_val] += accidents_count

        results = []
        id_count = 0
        for geo_hash, category_data in grouped_by_geohash.items():
            # geo_hash_coordinate = calculate_center_coordinate(geo_hash)
            id_count = id_count + 1
            location = geo_hash
            result = {
                "geo_hash": geo_hash,
                "geojson": {
                    "type": "FeatureCollection",
                    "features": [
                        {
                            "type": "Feature",
                            "id": id_count,
                            "properties": {
                                "name": location,
                                "density": [
                                    (count / total_count) * 100
                                    for category_val, count in category_data.items()
                                    if category_val == category_value
                                ][0],
                            },
                            "geometry": {
                                "type": "Polygon",
                                "coordinates": [calculate_bounding_box(geo_hash)],
                            },
                        },
                    ],
                },
                f"{category_value}": [
                    (count / total_count) * 100
                    for category_val, count in category_data.items()
                    if category_val == category_value
                ],
            }
            results.append(result)

        return JsonResponse({"Result": results})
