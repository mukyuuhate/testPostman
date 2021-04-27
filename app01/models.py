from django.db import models

# Create your models here.

# 创建登录用户的实体
class User(models.Model):
    # 创建实体类属性和数据库表的字段对应
    # 用户编号,是主键
    userno = models.AutoField(primary_key=True)
    # 账号
    uaccount = models.CharField(max_length=64)
    # 密码
    upassword = models.CharField(max_length=64)
