from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import CustomUserManager
from django.utils import timezone

class NewUser(AbstractBaseUser, PermissionsMixin):
    
    username = models.CharField(verbose_name='Username', max_length=50, unique=True)
    email = models.EmailField(verbose_name='Email', unique=True)
    id_number = models.IntegerField(verbose_name='ID Number', unique=True, null=True, blank=True)
    job = models.CharField(verbose_name='Job', max_length=100, null=True, blank=True)
    address = models.CharField(verbose_name='Address', max_length=250, null=True, blank=True)
    city = models.CharField(verbose_name='City', max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True,null=True,blank=True)
    is_staff = models.BooleanField(default=False,null=True,blank=True)
    is_superuser = models.BooleanField(default=False,null=True,blank=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.username






