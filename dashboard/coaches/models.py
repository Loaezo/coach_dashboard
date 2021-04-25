from django.db import models
from django.contrib.auth.models import User
import uuid

class Coach(models.Model):

    """ Coach Model

    Proxy model that extends the base data with other information """

    coach = models.OneToOneField(User, on_delete=models.CASCADE, default=None)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=50, blank=True)
    role_choice = {
        ('Tech Coach', 'Tech Coach'),
        ('Talent Placement Coach', 'Talent Placement Coach'),
        ('Academic Coach', 'Academic Coach')
    }
    role = models.CharField(max_length=100, choices=role_choice)
    description = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    location = models.CharField(max_length=50, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'coach'
        verbose_name_plural = 'coaches'
        ordering = ['-created']

    def __str__(self):
        return self.coach.username