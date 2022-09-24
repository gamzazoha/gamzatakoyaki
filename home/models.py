from django.db import models

# Create your models here.

class Offers(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='appname', null=True)
    region = models.CharField(max_length=20)
    created_date = models.DateTimeField()

    def __str__(self):
        return self.name