from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    age = models.CharField(max_length=10)

class Date(models.Model):
    attenddate = models.DateField(verbose_name='打刻日')
    class Meta:
        db_table = 'date'

class Attendance(models.Model):

    class Meta:
        db_table = 'attendance'

    IN_OUT = (
        ('出勤', '出勤'),
        ('退勤', '退勤'),
        ('休憩開始', '休憩開始'),
        ('休憩終了', '休憩終了'),
    )

    attend = models.CharField(max_length=100 ,choices=IN_OUT, default=None)
    time = models.TimeField(verbose_name="打刻時間")
    user_id = models.CharField(max_length=50, null=True) 
    Date = models.ForeignKey(Date, verbose_name="打刻日", on_delete=models.CASCADE, default=None)
    # member = models.ForeignKey(get_user_model(), verbose_name="メンバー", on_delete=models.CASCADE, default=None)