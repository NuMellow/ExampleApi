from rest_framework import serializers
from .models import Job, Driver

class JobSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Job
        fields =('id', 'truck_id', 'trailer_id', 'driver_id', 'source', 'destination', 'date_scheduled', 'date_created', 'status')
        read_only_fields = ('id', 'truck_id', 'trailer_id', 'driver_id', 'source', 'destination', 'date_scheduled', 'date_created' )

class DriverSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Driver
        fields = ('id', 'full_name', 'contact_number', 'license_number', 'province')
        read_only_fields = ('id', 'full_name', 'contact_number', 'license_number', 'province')