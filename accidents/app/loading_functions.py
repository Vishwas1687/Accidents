from .load_data import *
import random
import pygeohash as geohash
from datetime import datetime


def get_victim_age():
    n = 100
    age = random.randint(0, n)
    return age


def get_type_of_accident():
    n = len(type_of_accident)
    index = random.randint(0, n - 1)
    return type_of_accident[index]


def get_geohash_encode(latitude, longitude):
    precision = 6
    geohash_code = geohash.encode(latitude, longitude, precision=precision)
    return geohash_code


def get_area_type():
    n = len(area_type)
    index = random.randint(0, n - 1)
    return area_type[index]


def get_date(month, year):
    n = 0
    day = 0
    if year % 4 == 0 and year % 100 != 0 and month == "february":
        n = 29
        day = random.randint(1, n)
    elif year % 4 != 0 and month == "february":
        n = 28
        day = random.randint(1, n)
    elif (
        month == "january"
        or month == "march"
        or month == "may"
        or month == "july"
        or month == "august"
        or month == "october"
        or month == "decemnber"
    ):
        n = 32
        day = random.randint(1, n)
    else:
        n = 30
        day = random.randint(1, n)

    return day


def get_time():
    hour = random.randint(0, 23)
    minute = random.randint(0, 59)
    second = random.randint(0, 59)
    return datetime.strptime(f"{hour:02d}:{minute:02d}:{second:02d}", "%H:%M:%S").time()


def get_coordinates():
    latitude = round(random.uniform(south_west_latitude, north_east_latitude), 4)
    longitude = round(random.uniform(south_west_longitude, north_east_longitude), 4)
    return latitude, longitude


def get_month():
    n = len(month)
    index = random.randint(0, n - 1)
    return month[index]


def get_year():
    n = len(year)
    index = random.randint(0, n - 1)
    return year[index]


def get_weather_condition():
    n = len(weather_condition)
    index = random.randint(0, n - 1)
    return weather_condition[index]


def get_type_of_road():
    n = len(type_of_road)
    index = random.randint(0, n - 1)
    return type_of_road[index]


def get_road_environment():
    n = len(road_environment)
    index = random.randint(0, n - 1)
    return road_environment[index]


def get_road_features():
    n = len(road_features)
    index = random.randint(0, n - 1)
    return road_features[index]


def get_junction_type():
    n = len(junction_type)
    index = random.randint(0, n - 1)
    return junction_type[index]


def get_traffic_control_at_junction():
    n = len(traffic_control_at_junction)
    index = random.randint(0, n - 1)
    return traffic_control_at_junction[index]


def get_pedestrian_infrastructure():
    n = len(pedestrian_infrastructure)
    index = random.randint(0, n - 1)
    return pedestrian_infrastructure[index]


def get_traffic_control_at_junction():
    n = len(traffic_control_at_junction)
    index = random.randint(0, n - 1)
    return traffic_control_at_junction[index]


def get_impacting_vehicle():
    n = len(impacting_vehicle)
    index = random.randint(0, n - 1)
    return impacting_vehicle[index]


def get_victim_vehicle():
    n = len(victim_vehicle)
    index = random.randint(0, n - 1)
    return victim_vehicle[index]


def get_type_of_collision():
    n = len(type_of_collision)
    index = random.randint(0, n - 1)
    return type_of_collision[index]


def get_type_of_impact():
    n = len(type_of_impact)
    index = random.randint(0, n - 1)
    return type_of_impact[index]


def get_type_of_traffic_violation():
    n = len(type_of_traffic_violation)
    index = random.randint(0, n - 1)
    return type_of_traffic_violation[index]


def get_license_of_drivers():
    n = len(license_of_drivers)
    index = random.randint(0, n - 1)
    return license_of_drivers[index]


def get_type_of_road_user():
    n = len(type_of_road_user)
    index = random.randint(0, n - 1)
    return type_of_road_user[index]
