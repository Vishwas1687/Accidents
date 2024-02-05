import pygeohash as geohash
from django.db.models import Q
from .models import Accident
from django.db.models import Count

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
            filter_query &= Q(**{field_name: field_value})
    return filter_query


def get_unique_category_values(category):
    return list(Accident.objects.values_list(category, flat=True).distinct())


def group_location_and_category_heirarchial(filtered_accidents, category):
    return filtered_accidents.values("geo_hash", f"{category}").annotate(
        accidents=Count(f"{category}")
    )


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


def populate_geohash_category_accidents_map(
    accidents_grouped_by_geohash, grouped_by_geohash, category
):
    for item in accidents_grouped_by_geohash:
        geo_hash = item["geo_hash"]
        category_val = item[f"{category}"]
        accidents_count = item["accidents"]

        grouped_by_geohash[geo_hash][category_val] += accidents_count
    return grouped_by_geohash
