# coding=utf-8
from django.db import models
from gu_db.base_model import BaseModel
from gu_db.base_manager import BaseModelManager
# Create your models here.


# 账号类
class Passport(BaseModel):
    username = models.CharField(max_length=20, help_text='用户名')
    password = models.CharField(max_length=40, help_text='密码')
    email = models.EmailField(help_text='邮箱')

    # 创建一个自定义模型管理器的对象
    objects = PassportManager()

    class Meta:
        db_table = 's_user_account'


# 账户模型管理器
class PassportManager(BaseModelManager):
    # 添加账户
    def add_one_passport(self, username, password, email):

        obj = self.create_one_object(username=username, password=password, email=email)
        return obj







