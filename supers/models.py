from django.db import models
from super_types.models import SuperType

# Create your models here.
class Power(models.Model):
    name = models.CharField(max_length=50)

class Super(models.Model):
    name = models.CharField(max_length=30)
    alter_ego = models.CharField(max_length=30)
    power = models.ManyToManyField(Power)
    catchphrase = models.CharField(max_length=50)
    super_type = models.ForeignKey(SuperType, on_delete=models.CASCADE)

