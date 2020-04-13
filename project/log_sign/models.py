from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class normal_user(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    student_number = models.CharField(blank=True, max_length=50)
    phone = models.CharField(blank=True, max_length=50)
    class Meta:
        verbose_name_plural = 'normal_user'
