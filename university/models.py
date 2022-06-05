from django.db import models


class Faculty(models.Model):
    name = models.CharField(max_length=10)


class Category(models.Model):
    name = models.CharField(max_length=10)


class Curriculum(models.Model):
    name = models.CharField(max_length=20)
    credit = models.IntegerField(help_text='学分')
    semester = models.CharField(max_length=20, help_text='开课学期')
    limitation = models.IntegerField(help_text='人数上限')
    selected = models.IntegerField(help_text='已选人数')
    requirement = models.TextField(default='', help_text='课程要求')
    introduction = models.TextField(default='', help_text='课程介绍')
    remark = models.TextField(default='', help_text='课程备注')
    schedule = models.JSONField(help_text='课程时间')
    state = models.SmallIntegerField(default=0, help_text='课程状态')
    create_time = models.DateTimeField(auto_now_add=True)
    faculty = models.ForeignKey('Faculty', on_delete=models.CASCADE)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
