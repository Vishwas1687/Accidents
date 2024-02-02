from rest_framework import serializers
from app.models import *


class AccidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accident
        fields = "__all__"
