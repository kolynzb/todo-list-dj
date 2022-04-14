from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=225)
    text = models.TextField(max_length=225)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def _str(self):
        return self.title


class District(models.Model):
    name = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Organization(models.Model):
    facility_name = models.CharField(max_length=400)
    phone_number = models.CharField(max_length=400)
    district = models.ForeignKey(District, on_delete=models.DO_NOTHING)
    address = models.CharField(max_length=300)
    open_hour = models.CharField(max_length=100)
    close_hour = models.CharField(max_length=100)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, default=0.3476)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, default=32.5825)
    link = models.CharField(max_length=400)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.facility_name
