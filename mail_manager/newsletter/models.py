from __future__ import unicode_literals

from django.db import models

User = 'auth.User'


class Subscriber(models.Model):
    name = models.CharField(
        max_length=32
    )
    surname = models.CharField(
        max_length=32
    )
    email = models.EmailField(
        unique=True,
        db_index=True
    )
    birth_date = models.DateField()


class Newsletter(models.Model):
    name = models.CharField(
        max_length=32,
        db_index=True
    )
    content = models.TextField()
    subscribers = models.ManyToManyField(
        Subscriber,
        blank=True
    )
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='newsletters'
    )
