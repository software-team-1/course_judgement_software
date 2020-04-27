# Create your models here.
from django.db import models
from log_sign.models import normal_user
import datetime


class course(models.Model):
    # 课程名
    name = models.CharField(max_length=20, null=False)
    # 授课教师
    teacher = models.CharField(max_length=10, null=False)
    credit =models.DecimalField(max_digits=10,decimal_places=1,default=2)
    def __unicode__(self):
        return self.name


class judgement_system(models.Model):
    name = models.ForeignKey(normal_user, on_delete=models.CASCADE)
    course = models.ForeignKey(course, on_delete=models.CASCADE)
    create_date = models.DateTimeField(default=datetime.datetime.now())
    evaluation = models.CharField(max_length=500, null=False)