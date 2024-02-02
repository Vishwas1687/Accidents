import csv
import os
from app.models import *
from app.loading_functions import *


def run():
    file = open("D:\Accidents Mini project\Load_data.csv")
    accidents_file = csv.reader(file)
    Accident.objects.all().delete()
    count = 1
    for records in accidents_file:
        if count == 1:
            pass
        else:
            type_of_accident = get_type_of_accident()
            time = get_time()
            month = get_month()
            year = get_year()
            date = get_date(month, year)
            latitude, longitude = get_coordinates()
            area_type = get_area_type()
            weather_condition = get_weather_condition()
            type_of_road = get_type_of_road()
            road_environment = get_road_environment()
            junction_type = get_junction_type()
            traffic_control_at_junction = get_traffic_control_at_junction()
            pedestrian_infrastructure = get_pedestrian_infrastructure()
            impacting_vehicle = get_impacting_vehicle()
            victim_vehicle = get_victim_vehicle()
            type_of_collision = get_type_of_collision()
            type_of_impact = get_type_of_impact()
            type_of_traffic_violation = get_type_of_traffic_violation()
            type_of_road_user = get_type_of_road_user()
            license_of_drivers = get_license_of_drivers()
            victim_age = get_victim_age()
            geo_hash = get_geohash_encode(latitude, longitude)

            Accident.objects.create(
                type_of_accident=type_of_accident,
                time=time,
                date=date,
                month=month,
                year=year,
                latitude=latitude,
                longitude=longitude,
                area_type=area_type,
                weather_condition=weather_condition,
                type_of_road=type_of_road,
                road_environment=road_environment,
                junction_type=junction_type,
                traffic_control_at_junction=traffic_control_at_junction,
                pedestrian_infrastructure=pedestrian_infrastructure,
                impacting_vehicle=impacting_vehicle,
                victim_vehicle=victim_vehicle,
                type_of_collision=type_of_collision,
                type_of_impact=type_of_impact,
                type_of_traffic_violation=type_of_traffic_violation,
                type_of_road_user=type_of_road_user,
                license_of_drivers=license_of_drivers,
                victim_age=victim_age,
                geo_hash=geo_hash,
            )

        count = count + 1
