from django.db import models
from django.utils import timezone

# Create your models here.
class Fetch(models.Model):
	created = models.DateTimeField(default=timezone.now())

