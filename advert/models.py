from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class Advert(models.Model):
    ADVERT_STATUS_CHOICES = (
        ('Running', 'Running'),
        ('Stopped', 'Stopped'),
    )
    ADVERT_SUBSCRIPTION_CHOICES = (
        ('Week', 'Week'),
        ('Monthly', 'Monthly'),

    )
    user = models.ForeignKey(User,
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

    slug = models.SlugField(blank=True, null=True, max_length=200)

    def save(self, *args, **kwargs):
        if not self.slug and self.title:
            self.slug = slugify(self.title)
        super(Advert, self).save(*args, **kwargs)

    def __str__(self):
        return self.title
