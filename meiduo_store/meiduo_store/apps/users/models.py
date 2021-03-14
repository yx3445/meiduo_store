from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    """自定义模型类"""
    model = models.CharField(max_length=11,unique=True,verbose_name='手机号')

    class Meta: # 配置数据库表名及设置模型在admin站点显示的中文名
        db_table = 'tb_users'
        verbose_name = '用户'
        verbose_name_plural = verbose_name
