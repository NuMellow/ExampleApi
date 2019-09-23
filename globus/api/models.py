from django.db import models
from django.utils import timezone

class Load(models.Model):
  """docstring for List"""
  # user = models.ForeignKey('User', on_delete=models.CASCADE)
  item = models.CharField(max_length=200)
  verified = models.BooleanField(default=False)
  # cargo_owner = models.ForeignKey(Cargoowner, models.DO_NOTHING)
  pick_up_location = models.ForeignKey('Location', models.SET_NULL, db_column='pick_up_location', blank=True, null=True, related_name='pick_up')
  drop_off_location = models.ForeignKey('Location', models.SET_NULL, db_column='drop_off_location', blank=True, null=True, related_name='drop_off')
  load_type = models.ForeignKey('Loadtype', models.SET_NULL, db_column='load_type', blank=True, null=True)
  # load_status = models.ForeignKey('Loadstatus', models.DO_NOTHING)
  tonnage = models.FloatField(null=True)
  pick_up_date = models.DateField(null=True)
  date_posted = models.DateField(default=timezone.now)
  additional_info = models.CharField(max_length=200, blank=True, null=True)
  pick_up_notes = models.CharField(max_length=200, blank=True, null=True)
  drop_off_notes = models.CharField(max_length=200, blank=True, null=True)
  attachment = models.BinaryField(null=True)
  staged = models.BooleanField(default=False)
  job_id = models.ForeignKey('Job', models.SET_NULL, db_column='job_id', blank=True, null=True)

  PENDING = 'PE'
  STARTED = 'ST'
  AT_PICKUP = 'AP'
  LOADING = 'LO'
  LOADED = 'CLO'
  IN_TRANSIT = 'IT'
  AT_DESTINATION = 'AD'
  OFFLOADING = 'OF'
  OFFLOADED = 'COF'
  COMPLETED = 'CO'

  JOB_STATUS_CHOICES = [
    (PENDING, 'Pending'),
    (STARTED, 'Started'),
    (AT_PICKUP, 'At Pickup'),
    (LOADING, 'Loading'),
    (LOADED, 'Loaded'),
    (IN_TRANSIT, 'In Transit'),
    (AT_DESTINATION, 'At Destination'),
    (OFFLOADING, 'Offloading'),
    (OFFLOADED, 'Offloaded'),
    (COMPLETED, 'Completed'),
  ]

  job_status = models.CharField(max_length=100, choices=JOB_STATUS_CHOICES, default=PENDING)
  def __str__(self):
    return self.item + ' | ' + str(self.verified)


class Loadstatus(models.Model):
    load_status_id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=100)

    class Meta:
        managed = False
        db_table = 'LoadStatus'


class Loadtype(models.Model):
    load_type = models.CharField(max_length=200)
    visible = models.BooleanField(default=True)

    class Meta:
        managed = True
        db_table = 'LoadType'

class Location(models.Model):
  address = models.CharField(max_length=100)
  area = models.CharField(max_length=100)
  city = models.CharField(max_length=100)
  coordinates = models.CharField(max_length=20)
  visible = models.BooleanField(default=True)
  # cargo_owner = models.ForeignKey(CargoOwner, models.DO_NOTHING)

class Truck(models.Model):
  plate_number = models.CharField(max_length=20)
  truck_make = models.CharField(max_length=200)
  truck_type = models.CharField(max_length=200)
  truck_model = models.CharField(max_length=200)
  tonnage = models.FloatField()
  visible = models.BooleanField(default=True)

def get_sentinel_truck():
  return Truck.objects.get_or_create(plate_number='deleted',truck_make='deleted', 
  truck_type='deleted', truck_model='deleted', tonnage=0, visible=False)[0]

class Trailer(models.Model):

  plate_number = models.CharField(max_length=20)
  trailer_type = models.CharField(max_length=200)
  tonnage = models.FloatField()
  visible = models.BooleanField(default=True)
  #white_book = models.FileField(upload_to=None, max_length=100)
  #company = models.ForeignKey(transporter, models.DO_NOTHING, db_column='id')

def get_sentinel_trailer():
  return Trailer.objects.get_or_create(plate_number='deleted',trailer_type='deleted', 
  tonnage=0, visible=False)[0]

class Keypersonnel(models.Model):

  full_name = models.CharField(max_length=200)
  contact_number =models.CharField(max_length=10)
  email = models.EmailField(max_length=254)
  position = models.CharField(max_length=200)
  visible = models.BooleanField(default=True)
  #address = models.ForeignKey(Location, models.DO_NOTHING, db_column='address')
class Driver(models.Model):
  full_name = models.CharField(max_length=100)
  contact_number = models.CharField(max_length=14)  
  nrc = models.CharField(max_length=50)
  short_nrc = models.CharField(max_length=4)
  license_number = models.CharField(max_length=50)
  # address = models.CharField(max_length=100)
  # city = models.CharField(max_length=100)
  province = models.CharField(max_length=100)
  # attached_license = models.BinaryField(null=True)
  # company_name = models.ForeignKey(Users, models.DO_NOTHING)
  visible = models.BooleanField(default=True)

def get_sentinel_driver():
  return Driver.objects.get_or_create(full_name='deleted',contact_number='deleted', 
  nrc='deleted', license_number='deleted', province='deleted', visible=False)[0]

class Job(models.Model):
  truck_id = models.ForeignKey('Truck', models.SET(get_sentinel_truck), blank=True, null=True, db_column='truck_id')
  trailer_id = models.ForeignKey('Trailer', models.SET(get_sentinel_trailer), blank=True, null=True, db_column='trialer_id')
  driver_id = models.ForeignKey('Driver', models.SET(get_sentinel_driver), blank=True, null=True, db_column='driver_id')
  # source = models.ForeignKey('Location', models.DO_NOTHING, blank=True, null=True, db_column='id', related_name='source_id')
  # destination = models.ForeignKey('Location', models.DO_NOTHING, blank=True, null=True, db_column='id', related_name='destination_id')
  source = models.CharField(max_length=100)
  destination = models.CharField(max_length=100)
  date_scheduled = models.DateField(blank=True, null=True)
  date_created = models.DateTimeField(default=timezone.now)
  status = models.CharField(max_length=100, default='Pending')
