from django.contrib.auth.models import AbstractUser, UserManager
from django.db import models


class CustomUserManager(UserManager):
    def create_user(self, username, email=None, password=None, **extra_fields):

        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(username, email, password, **extra_fields)


class User(AbstractUser):
    department = models.ForeignKey('Department', on_delete=models.CASCADE)
    gender = models.BooleanField(default=False)
    title = models.CharField(default='', help_text='职称')
    enrollment_year = models.IntegerField(default=0, help_text='入学年份')

    objects = CustomUserManager()

