from django.db import models
from django.contrib.auth.models import User
import uuid

class Coach(models.Model):

""" Coach Model

Proxy model that extends the base data with other information """

    coach = models.OneToOneField(User, on_delete=models.CASCADE)

    
    coach_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    role = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=50)
    location = models.CharField(max_length=50)