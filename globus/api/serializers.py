from rest_framework import serializers
from .models import Job, Driver, Load

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

class LoadSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Load
        fields = ('id', 'item', 'verified', 'pick_up_location', 'drop_off_location', 'load_type', 'tonnage', 'pick_up_date', 'additional_info', 'pick_up_notes', 'drop_off_notes', 'job_id', 'job_status')
        read_only_fields = ('id', 'item', 'verified', 'pick_up_location', 'drop_off_location', 'load_type', 'tonnage', 'pick_up_date', 'additional_info', 'pick_up_notes', 'drop_off_notes', 'job_id')