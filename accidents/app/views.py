from django.shortcuts import render
from rest_framework.views import APIView
from django.http import JsonResponse
from django.conf import settings
from .models import Accident
from .utilFunctions import (
    calculate_bounding_box,
    prepare_filter,
    get_unique_category_values,
    group_location_and_category_heirarchial,
    initialize_grouped_by_geohash,
    group_category_only,
    populate_geohash_category_accidents_map,
)
from django.db.models import Count
from django.db.models import Q
from .serializer import *
import json
import redis

# Create your views here.
redis_instance = redis.StrictRedis(
    host=settings.REDIS_HOST, port=settings.REDIS_PORT, db=0
)


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
        distinct_values = []
        key = f"unique_values:{category}"
        value = redis_instance.get(key)
        result_map = {}
        if value:
            result_map = json.loads(value)
        else:
            distinct_values = get_unique_category_values(category)
            all_accidents = Accident.objects.all()
            result_map = {str(value): [] for value in distinct_values}

            for acc in all_accidents:
                category_value = str(getattr(acc, category))
                result_map[category_value].append(
                    [str(acc.latitude), str(acc.longitude)]
                )

            redis_instance.set(key, json.dumps(result_map))

        return JsonResponse({"result_map": result_map}, safe=False)


class AccidentCategoryViewWithCrossFilters(APIView):
    def get(self, request, category):
        filters = request.GET.get("filters", [])
        filters = json.loads(filters)
        final_filter = prepare_filter(filters)
        key = f"accident-category-with-cross-filters:{category}:{filters}"
        value = redis_instance.get(key)
        result_map = {}
        if value:
            result_map = json.loads(value)
        else:
            all_accidents = Accident.objects.filter(final_filter)

            distinct_values = get_unique_category_values(category)
            result_map = {value: [] for value in distinct_values}
            for acc in all_accidents:
                category_value_in_acc = getattr(acc, category)
                result_map[category_value_in_acc].append(
                    [str(acc.latitude), str(acc.longitude)]
                )
            redis_instance.set(key, json.dumps(result_map))
        return JsonResponse({"result_map": result_map}, safe=False)


class AccidentGroupedByPercentageLocation(APIView):
    def get(self, request, category):
        filtered_accidents = []
        filters = request.GET.get("filters", "[]")
        comparator = request.GET.get("comparator")
        if len(filters) != 0:
            filters = json.loads(filters)
            final_filter = prepare_filter(filters)
            filtered_accidents = Accident.objects.filter(final_filter)
        else:
            filtered_accidents = Accident.objects.all()

        key = (
            f"accident-grouped-by-percentage-location:{category}:{comparator}:{filters}"
        )
        value = redis_instance.get(key)
        results = []
        if value:
            results = json.loads(value)
        else:
            accidents_grouped_by_geohash = group_location_and_category_heirarchial(
                filtered_accidents, category
            )

            grouped_by_geohash = {}
            geo_hashes = get_unique_category_values("geo_hash")
            category_values = get_unique_category_values(category)

            grouped_by_geohash = initialize_grouped_by_geohash(
                geo_hashes, category_values
            )

            grouped_by_geohash = populate_geohash_category_accidents_map(
                accidents_grouped_by_geohash, grouped_by_geohash, category
            )

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
                    percentage_comparison = (
                        (comparator_count * 1.0) / total_count
                    ) * 100

                result = {
                    "geo_hash": geo_hash,
                    f"percentage {comparator}": percentage_comparison,
                }
                results.append(result)

            redis_instance.set(key, json.dumps(results))

        return JsonResponse({"accidents_grouped_by_geohash": results}, safe=False)


class AccidentCategoryPercentageByLocation(APIView):
    def get(self, request, category, category_value):
        filtered_accidents = []
        filters = request.GET.get("filters", "[]")
        if len(filters) != 0:
            filters = json.loads(filters)
            final_filter = prepare_filter(filters)
            filtered_accidents = Accident.objects.filter(final_filter)
        else:
            filtered_accidents = Accident.objects.all()
        key = f"accident-category-percentage-by-location:{category}:{category_value}:{filters}"
        value = redis_instance.get(key)
        results = []
        if value:
            results = json.loads(value)
        else:
            category_value_count = group_category_only(filtered_accidents, category)
            total_count = 0
            for items in category_value_count:
                category_val = items[f"{category}"]
                count = items["count"]
                if category_val == category_value:
                    total_count = count
            accidents_grouped_by_geohash = group_location_and_category_heirarchial(
                filtered_accidents, category
            )

            grouped_by_geohash = {}
            geo_hashes = get_unique_category_values("geo_hash")
            category_values = get_unique_category_values(category)
            grouped_by_geohash = initialize_grouped_by_geohash(
                geo_hashes, category_values
            )

            grouped_by_geohash = populate_geohash_category_accidents_map(
                accidents_grouped_by_geohash, grouped_by_geohash, category
            )

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
            redis_instance.set(key, json.dumps(results))
        return JsonResponse({"Result": results})


class AccidentGroupedCategoryByCumulative(APIView):
    def get(self, request, category):
        filtered_accidents = []
        filters = request.GET.get("filters", "[]")
        if len(filters) != 0:
            filters = json.loads(filters)
            final_filter = prepare_filter(filters)
            filtered_accidents = Accident.objects.filter(final_filter)
        else:
            filtered_accidents = Accident.objects.all()

        key = f"accidents-grouped-category-by-cumulative:{category}:{filters}"
        value = redis_instance.get(key)
        results = []
        if value:
            results = json.loads(value)
        else:
            accidents_grouped_by_geohash = group_location_and_category_heirarchial(
                filtered_accidents, category
            )

            grouped_by_geohash = {}
            geo_hashes = get_unique_category_values("geo_hash")
            category_values = get_unique_category_values(category)
            grouped_by_geohash = initialize_grouped_by_geohash(
                geo_hashes, category_values
            )

            grouped_by_geohash = populate_geohash_category_accidents_map(
                accidents_grouped_by_geohash, grouped_by_geohash, category
            )

            id_count = 0
            for geo_hash, category_data in grouped_by_geohash.items():
                location = geo_hash
                id_count = id_count + 1
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
                                    f"{category}": [
                                        {"type": category, "accidents": count}
                                        for category, count in category_data.items()
                                    ],
                                },
                                "geometry": {
                                    "type": "Polygon",
                                    "coordinates": [calculate_bounding_box(geo_hash)],
                                },
                            },
                        ],
                    },
                }
                results.append(result)

            redis_instance.set(key, json.dumps(results))

        return JsonResponse({"accidents_grouped_by_geohash": results}, safe=False)
