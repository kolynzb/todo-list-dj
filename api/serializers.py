from rest_framework import serializers
from .models import Todo , District ,Organization

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = '__all__'


class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ('name',)

class OrganizationSerializer(serializers.ModelSerializer):
    district = DistrictSerializer(many=False, read_only=True)
    district_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Organization
        fields = '__all__'

