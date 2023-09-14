from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
# Create your models here.

class CustomUser(AbstractUser):
    phone_number = models.CharField(
    max_length=16,
    blank=True,
    null=True,
    validators=[
    RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format '+123456789'. Up to 15 digits allowed."
    ),],)
    
    CHOISE_ROLES = (
        (2, 'admin'),
        (1, 'user')
    )
    roles = models.PositiveSmallIntegerField(default=1, choices=CHOISE_ROLES)

