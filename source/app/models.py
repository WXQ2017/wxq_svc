from django.db import models

# Create your models here.

class Testdb(models.Model):
    name = models.CharField(max_length=20)
# 一般来说，每一个模型都映射一张数据库表。
# 每个模型都是一个 Python 的类，这些类继承 django.db.models.Model
# 模型类的每个属性都相当于一个数据库的字段。
# 利用这些，Django 提供了一个自动生成访问数据库的 API；exit

# class User(models.Model):
#     name = models.CharField(max_length=20)
#     password = models.CharField(max_length=20)
#     create_time = models.DateField(auto_now=False)
#     update_time = models.DateField(auto_now=False)
#     status = models.IntegerField()
#     is_deleted = models.IntegerField()

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
