from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_ADMIN = 'admin'
    ROLE_STAFF = 'staff'
    ROLE_ENTREPRENEUR = 'entrepreneur'
    ROLE_VISITOR = 'visitor'

    ROLE_CHOICES = [
        (ROLE_ADMIN, 'Admin'),
        (ROLE_STAFF, 'Staff'),
        (ROLE_ENTREPRENEUR, 'Entrepreneur'),
        (ROLE_VISITOR, 'Visitor'),
    ]

    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default=ROLE_VISITOR)
    phone = models.CharField(max_length=20, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    bio = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.email or self.username
