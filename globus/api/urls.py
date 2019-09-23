from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns
from .views import DetailsView, ListView, DriverListView, DriverDetailsView, DriverJobsListView, LoadListView, LoadDetailsView

urlpatterns = {
    #url(r'^jobs/(?P<pk>[0-9]+)/$', DetailsView.as_view(), name="details"),
    path('jobs/<int:pk>/', DetailsView.as_view(), name="details"),
    path('jobs/', ListView.as_view(), name="details"),
    path('drivers/', DriverListView.as_view(), name="details"),
    path('driver/<contact_number>/<short_nrc>/', DriverDetailsView.as_view(), name="details"),
    path('driver_jobs/<int:driver_id>', DriverJobsListView.as_view(), name="details"),
    path('loads/<int:job_id>', LoadListView.as_view(), name="details"),
    path('load/<int:pk>', LoadDetailsView.as_view(), name="details")
}

urlpatterns = format_suffix_patterns(urlpatterns)