from django.contrib.auth.models import AbstractUser,Group,Permission
from django.db import models

class CustomUser(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.username
    groups = models.ManyToManyField(
        Group,
        related_name='customuser_groups',  # change the related_name
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='customuser_permissions',  # change the related_name
        blank=True,
    )