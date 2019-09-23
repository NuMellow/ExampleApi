from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .serializers import JobSerializer, DriverSerializer, LoadSerializer
from .models import Job, Driver, Load


from django.shortcuts import get_object_or_404, get_list_or_404

class ListView(generics.ListAPIView):
    """This class handles the http GET (all) reuests."""

    queryset = Job.objects.all()
    serializer_class = JobSerializer

class DetailsView(generics.RetrieveUpdateAPIView):
    """This class handles the http GET and PUT requests."""

    queryset = Job.objects.all()
    serializer_class = JobSerializer

class DriverListView(generics.ListAPIView):

    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

class MultipleFieldLookupMixin(object):
    """Apply this mixin to any view or viewset to get multiple field filtering based
    on a 'lookup_fields' attribute, instead of the default single field filtering."""

    def get_object(self):
        queryset = self.get_queryset()
        queryset = self.filter_queryset(queryset)
        filter = {}
        for field in self.lookup_fields:
            if self.kwargs[field]:
                filter[field] = self.kwargs[field]
        obj = get_object_or_404(queryset, **filter)
        self.check_object_permissions(self.request, obj)
        return obj

class DriverDetailsView(MultipleFieldLookupMixin, generics.RetrieveAPIView):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    lookup_fields = ['contact_number', 'short_nrc'] 

class DriverJobsListView(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    lookup_fields = ['driver_id']

    def list(self, request, driver_id):
        queryset = self.get_queryset()
        queryset = queryset.filter(driver_id=driver_id)
        serializer = JobSerializer(queryset, many=True)
        return Response(serializer.data)

class LoadListView(generics.ListAPIView):
    queryset = Load.objects.all()
    serializer_class = LoadSerializer
    lookup_fields = ['job_id']

    def list(self, request, job_id):
        queryset = self.get_queryset()
        queryset = queryset.filter(job_id=job_id)
        serializer = LoadSerializer(queryset, many=True)
        return Response(serializer.data)

class LoadDetailsView(generics.RetrieveUpdateAPIView):
    """This class handles the http GET and PUT requests."""

    queryset = Load.objects.all()
    serializer_class = LoadSerializer