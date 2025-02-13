from __future__ import unicode_literals

from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Subscription(models.Model):
    subscriber = models.EmailField()
    author = models.ForeignKey(
        User,
        related_name='subs',
        on_delete=models.CASCADE
    )
