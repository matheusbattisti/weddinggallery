from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.contrib.auth.models import User

class Profile(models.Model):
    
    STATUS = (
        ('yes', 'Yes'),
        ('no', 'No'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    isGuest = models.CharField(
        max_length=3,
        choices=STATUS,
        default='yes'
    )
