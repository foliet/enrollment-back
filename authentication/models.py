from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    gender = models.BooleanField(default=False)
    identity = models.IntegerField(default=0, help_text="学生/教师/教务")
    title = models.CharField(default='', max_length=10, help_text='职称')
    enrollment_year = models.IntegerField(default=0, help_text='入学年份')
    faculty = models.ForeignKey('university.Faculty', on_delete=models.CASCADE)

    class Meta(AbstractUser.Meta):
        db_table = 'auth_user'
