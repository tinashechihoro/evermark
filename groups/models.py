from django.contrib.auth.models import User
from django.db import models


class GroupCategory(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='group_category_images/')

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='group_images/')
    category = models.ForeignKey(GroupCategory, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class Message(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    text_message = models.TextField()

    def __str__(self):
        return self.text_message

class MessegeComment(models.Model):
    message =  models.ForeignKey(Message,on_delete=models.DO_NOTHING)
    comment =  models.TextField()

    def __str__(self):
        return self.comment