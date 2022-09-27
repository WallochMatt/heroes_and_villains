from django.db import models
from super_types.models import SuperType

# Create your models here.

class Super(models.Model):
    name = models.CharField(max_length=30)
    alter_ego = models.CharField(max_length=30)
    primary_ability = models.CharField(max_length=30)
    secondary_ability = models.CharField(max_length=30)
    catchphrase = models.CharField(max_length=50)
    super_type = models.ForeignKey(SuperType, on_delete=models.CASCADE)