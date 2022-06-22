from django.db import models
from datetime import datetime
from pyexpat import model


# Create your models here.
class AppUser(models.Model):
    first_name = models.CharField(max_length=100)
    middle_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=20)
    dob = models.DateField()
    password = models.CharField(max_length=100)
    profile_pic = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    verification_code = models.CharField(max_length=8)
    is_verified = models.BooleanField(default=False)
    is_removed = models.BooleanField(default=False)
    created_at = models.DateTimeField(default=0)
    updated_at = models.DateTimeField(null=True)
    removed_at = models.DateTimeField(null=True)

    class Meta:
        db_table = "app_user"


class WeatherType(models.Model):
    weather_type = models.CharField(max_length=100)

    class Meta:
        db_table = "app_weather_type"


class Weather(models.Model):
    weather_type = models.BigIntegerField(max_length=20)
    user = models.BigIntegerField(max_length=20)
    address = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    updated_at = models.DateTimeField(default=0)

    class Meta:
        db_table = "app_weather"



