# coding=utf-8

from django.db import models


# 用户抽象模型类
class BaseModel(models.Model):
    create_time = models.DateTimeField(auto_now_add=True, help_text='创建时间')
    update_time = models.DateTimeField(auto_now=True, help_text='更新时间')
    is_delete = models.BooleanField(default=False, help_text='删除标记')

    class Meta:
        abstract = True  # 设置模型为抽象

