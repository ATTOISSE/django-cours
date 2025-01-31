from django.db import models
from django.contrib.auth.models import AbstractUser,Group,Permission

class CustomerUser(AbstractUser):
    groups = models.ManyToManyField(
        Group,
        related_name='users',
        related_query_name='user',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='users',
        related_query_name='user',
        blank=True
    )
