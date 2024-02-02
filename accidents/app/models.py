from django.db import models


# Create your models here.
class Accident(models.Model):
    id = models.AutoField(primary_key=True)
    type_of_accident = models.CharField(max_length=50)
    time = models.TimeField(auto_now=False, auto_now_add=False)
    date = models.PositiveIntegerField()
    month = models.CharField(max_length=50)
    year = models.PositiveIntegerField()
    latitude = models.DecimalField(max_digits=7, decimal_places=4)
    longitude = models.DecimalField(max_digits=7, decimal_places=4)
    area_type = models.CharField(max_length=50)
    weather_condition = models.CharField(max_length=50)
    type_of_road = models.CharField(max_length=50)
    road_environment = models.CharField(max_length=50)
    road_features = models.CharField(max_length=50)
    junction_type = models.CharField(max_length=50)
    traffic_control_at_junction = models.CharField(max_length=50)
    pedestrian_infrastructure = models.CharField(max_length=50)
    impacting_vehicle = models.CharField(max_length=50)
    victim_vehicle = models.CharField(max_length=50)
    type_of_collision = models.CharField(max_length=50)
    type_of_impact = models.CharField(max_length=50)
    type_of_traffic_violation = models.CharField(max_length=50)
    type_of_road_user = models.CharField(max_length=50)
    license_of_drivers = models.CharField(max_length=50)
    victim_age = models.CharField(max_length=50)
    geo_hash = models.CharField(max_length=50)

    def __str__(self):
        return f"[{self.latitude}, {self.longitude}]"
