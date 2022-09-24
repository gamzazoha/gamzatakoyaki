from django.db import models

# Create your models here.

class Offer(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    location = models.CharField(max_length=255)
    opened_time = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    call_number = models.CharField(max_length=255)
    map_image = models.ImageField(upload_to='appname', null=True)
    thumbnail_image = models.ImageField(upload_to='appname', null=True)
    image1 = models.ImageField(upload_to='appname', null=True)
    image2 = models.ImageField(upload_to='appname', null=True)

    def __str__(self):
        return self.name