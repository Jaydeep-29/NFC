from django.db import models
from django.utils.timezone import now

# Create your models here.
class NFC_Details(models.Model):
    uid = models.CharField(max_length=100,null=True,)
    latitude = models.CharField(max_length=100,null=True,)
    longitude = models.CharField(max_length=100,null=True,)
    created_date = models.DateTimeField(default=now)
    # created_by = models.CharField(max_length=100,null=True,)
    # updated_date = models.DateTimeField(null=True,)
    # updated_by =  models.CharField(max_length=100,null=True,)
    def __str__(self):
        return (self.uid)
    
    