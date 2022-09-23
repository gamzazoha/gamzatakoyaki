from email import contentmanager
from pyexpat import model
from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    created_at = models.DateField()
    # author : 추후 작성 예정