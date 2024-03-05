import pygeohash as geohash
from django.db.models import Q
from .models import Accident
from django.db.models import Count, Case, When, IntegerField

# from geopy.geocoders import Nominatim
def calculate_bounding_box(geo_hash):
    lat, lon, lat_err, lon_err = geohash.decode_exactly(geo_hash)
    min_lat = lat - lat_err
    max_lat = lat + lat_err
    min_lon = lon - lon_err
    max_lon = lon + lon_err
    sw_corner = (min_lon, min_lat)
    se_corner = (max_lon, min_lat)
    ne_corner = (
        max_lon,
        max_lat,
    )
    nw_corner = (min_lon, max_lat)
    return sw_corner, se_corner, ne_corner, nw_corner


# def calculate_center_coordinate(geo_hash):
#     lat, lon, lat_err, lon_err = geohash.decode_exactly(geo_hash)
#     return lat, lon


# def calculate_location_by_coordinate(coordinate):
#     lat = coordinate[0]
#     long = coordinate[1]
#     geolocator = Nominatim(user_agent="accidents")
#     location = geolocator.reverse(f"{lat}, {long}")
#     return location.address


def prepare_filter(filters):
    filter_query = Q()
    for filter_dict in filters:
        for field_name, field_value in filter_dict.items():
            if isinstance(field_value, dict):
                min_value = field_value["min"]
                max_value = field_value["max"]
                filter_query &= Q(**{f"{field_name}__gte": min_value})
                filter_query &= Q(**{f"{field_name}__lte": max_value})
            else:
                filter_query &= Q(**{field_name: field_value})
    return filter_query


def get_unique_category_values(category):
    return list(Accident.objects.values_list(category, flat=True).distinct())


def group_location_and_category_heirarchial(filtered_accidents, category):
    return filtered_accidents.values("geo_hash", f"{category}").annotate(
        accidents=Count(f"{category}")
    )


def group_location_category2_heirarchial(filtered_accidents, category1, category2):
    # if category1 == "victim_age":
    #     age_ranges = [
    #         (0, 10),
    #         (11, 20),
    #         (21, 30),
    #         (31, 40),
    #         (41, 50),
    #         (51, 60),
    #         (61, 70),
    #         (71, 80),
    #         (81, 90),
    #         (91, 100),
    #     ]

    #     age_conditions = [
    #         When(victim_age__range=(start, end), then=end) for start, end in age_ranges
    #     ]
    #     age_case = Case(
    #         *age_conditions,
    #         default=None,
    #         output_field=IntegerField(),
    #     )
    #     value = (
    #         filtered_accidents.annotate(age_group=age_case)
    #         .values("geo_hash", f"{category2}", "age_group")
    #         .annotate(accidents=Count(f"{category2}"))
    #     )
    #     return value
    # else:
    return filtered_accidents.values(
        "geo_hash", f"{category1}", f"{category2}"
    ).annotate(accidents=Count(f"{category2}"))


def group_category_only(filtered_accidents, category):
    return filtered_accidents.values(f"{category}").annotate(
        accidents=Count(f"{category}")
    )


def initialize_grouped_by_geohash(geo_hashes, category_values):
    grouped_by_geohash = {}
    for geo_hash in geo_hashes:
        grouped_by_geohash[geo_hash] = {}
        for category_val in category_values:
            grouped_by_geohash[geo_hash][category_val] = 0
    return grouped_by_geohash


def initialize2_grouped_by_geohash(geo_hashes, category1_values, category2_values):
    grouped_by_geohash = {}
    for geo_hash in geo_hashes:
        grouped_by_geohash[geo_hash] = {}
        for category1_val in category1_values:
            grouped_by_geohash[geo_hash][category1_val] = {}
            for category2_val in category2_values:
                grouped_by_geohash[geo_hash][category1_val][category2_val] = 0
    return grouped_by_geohash


def populate_geohash_category_accidents_map(
    accidents_grouped_by_geohash, grouped_by_geohash, category
):
    for item in accidents_grouped_by_geohash:
        geo_hash = item["geo_hash"]
        category_val = item[f"{category}"]
        accidents_count = item["accidents"]

        grouped_by_geohash[geo_hash][category_val] += accidents_count
    return grouped_by_geohash


def populate_geohash_category2_accidents_map(
    accidents_grouped_by_geohash, grouped_by_geohash, category1, category2
):

    for item in accidents_grouped_by_geohash:
        geo_hash = item["geo_hash"]
        category_val1 = item[f"{category1}"]
        category_val2 = item[f"{category2}"]
        accidents_count = item["accidents"]
        grouped_by_geohash[geo_hash][category_val1][category_val2] += accidents_count
    return grouped_by_geohash
