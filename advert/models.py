from django.contrib.auth.models import User
from django.db import models


class Advert(models.Model):
    ADVERT_STATUS_CHOICES = (
        ('Running', 'Running'),
        ('Stopped', 'Stopped'),
    )
    ADVERT_SUBSCRIPTION_CHOICES = (
        ('Week','Week'),
        ('Monthly','Monthly'),


    )
    user = models.OneToOneField(User,
                                on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    text = models.TextField()
    image = models.ImageField(upload_to='advert_images/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    advert_running_status = models.CharField(max_length=10,
                                             choices=ADVERT_STATUS_CHOICES)
    advert_active_subscription = models.CharField(max_length=10,
                                                  choices=ADVERT_SUBSCRIPTION_CHOICES)

    def __str__(self):
        return self.title
