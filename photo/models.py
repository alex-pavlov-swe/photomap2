from django.db import models

# Create your models here.


class Photo(models.Model):
    # id = models.AutoField(primary_key=True)
    title = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)
