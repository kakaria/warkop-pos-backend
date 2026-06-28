from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=255)
    username = None
       
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    # panggil dari file managers.py
    objects = CustomUserManager() #type:ignore
    
    
    # ribet amat ya pake TextChoices
    class Role(models.TextChoices):
        ADMIN = "ADM", _("Admin")
        KASIR = "KSR", _("Kasir")
        KUSTOMER = "KST", _("Kustomer")
        
    # taro di charfield
    role = models.CharField(
        max_length = 3,
        choices = Role.choices,
        default=Role.KUSTOMER
    )
