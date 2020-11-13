# -*- coding: utf-8 -*-

from django.http import HttpResponse
# import sys
# sys.path.append("D:\own-code\wxq_svc\model")
# import models
from app.models import Testdb


# 数据库操作
def testdb(request):
    test1 = Testdb(name='wxq')
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")