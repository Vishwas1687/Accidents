# Generated by Django 5.0.1 on 2024-02-02 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accident',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type_of_accident', models.CharField(max_length=50)),
                ('time', models.TimeField()),
                ('date', models.PositiveIntegerField()),
                ('month', models.CharField(max_length=50)),
                ('year', models.PositiveIntegerField()),
                ('latitude', models.DecimalField(decimal_places=4, max_digits=7)),
                ('longitude', models.DecimalField(decimal_places=4, max_digits=7)),
                ('area_type', models.CharField(max_length=50)),
                ('weather_condition', models.CharField(max_length=50)),
                ('type_of_road', models.CharField(max_length=50)),
                ('road_environment', models.CharField(max_length=50)),
                ('road_features', models.CharField(max_length=50)),
                ('junction_type', models.CharField(max_length=50)),
                ('traffic_control_at_junction', models.CharField(max_length=50)),
                ('pedestrian_infrastructure', models.CharField(max_length=50)),
                ('impacting_vehicle', models.CharField(max_length=50)),
                ('victim_vehicle', models.CharField(max_length=50)),
                ('type_of_collision', models.CharField(max_length=50)),
                ('type_of_impact', models.CharField(max_length=50)),
                ('type_of_traffic_violation', models.CharField(max_length=50)),
                ('type_of_road_user', models.CharField(max_length=50)),
                ('license_of_drivers', models.CharField(max_length=50)),
                ('victim_age', models.CharField(max_length=50)),
                ('geo_hash', models.CharField(max_length=50)),
            ],
        ),
    ]
