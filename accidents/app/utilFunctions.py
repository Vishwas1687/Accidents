import pygeohash as geohash

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
