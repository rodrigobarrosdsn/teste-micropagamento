from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    ROLE_CHOICES = (
        ("ordinary", "Ordinary"),
        ("shopkeepers", "Shopkeepers"),
    )

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="profile")
    name = models.CharField(max_length=255, null=False)
    role = models.CharField(
        max_length=11, choices=ROLE_CHOICES, default="ordinary", null=False)
    cpf = models.CharField(max_length=11, null=True, blank=True, unique=True)
    cnpj = models.CharField(max_length=14, null=True, blank=True, unique=True)
