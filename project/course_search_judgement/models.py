# Create your models here.
from django.db import models
from log_sign.models import normal_user
import datetime


class course(models.Model):
    # 课程名
    name = models.CharField(max_length=20, null=False)
    # 授课教师
    teacher = models.CharField(max_length=10, null=False)
    # 课程学分
    credit = models.DecimalField(max_digits=10, decimal_places=1)
    # 种类，即人文类还是社科类
    type = models.CharField(max_length=20)

    # def __unicode__(self):
    # return self.name


class judgement_system(models.Model):
    name = models.ForeignKey(normal_user, on_delete=models.CASCADE)
    course = models.ForeignKey(course, on_delete=models.CASCADE)
    create_date = models.DateTimeField(default=datetime.datetime.now())
    recommend_mark = models.DecimalField(max_digits=2, decimal_places=0)  # 推荐程度
    hard_core_mark = models.DecimalField(max_digits=2, decimal_places=0)  # 硬核程度
    mark_of_interest = models.DecimalField(max_digits=2, decimal_places=0)  # 无聊程度
    time_for_homework = models.CharField(max_length=100, null=False)  # 平时作业及用时
    the_constitution_of_grade = models.CharField(max_length=50, null=False)  # 综合分数组成
    comment_of_the_course = models.CharField(max_length=300, null=False)  # 课程体验及评价
    comment_of_the_teacher = models.CharField(max_length=300, null=False)  # 教师评价
