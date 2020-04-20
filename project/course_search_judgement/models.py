# Create your models here.
class course(models.Model):
    # 课程名
    name = models.CharField(max_length=20, null=False)
    # 授课教师
    teacher = models.CharField(max_length=10, null=False)