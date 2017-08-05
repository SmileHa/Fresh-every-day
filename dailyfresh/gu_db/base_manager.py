# coding=utf-8
from django.db import models
import copy


# 自定义模型管理器抽象类
class BaseModelManager(models.Manager):
    # 获取模型管理器所在模型类的属性列表

    def get_all_valid_fields(self):

        # 获取模型管理器类所在的模型
        cls = self.model
        # 获取cls模型类的属性列表
        attr_list = cls._meta.get_all_field_names()
        return attr_list

        # 往数据库中插入一条模型管理器对象所在的模型类数据
    def create_one_object(self, **kwargs):

        vaild_fields = self.get_all_valid_fields()
        kws = copy .copy(kwargs)
        # 去除模型中没有的属性
        for k in kws.keys():
            if k not in vaild_fields:
                kwargs.pop(k)

        # 获取模型管理器对象所在的模型类
        cls = self.model
        obj = cls(**kwargs)
        # 保存进数据库
        obj.save()
        return obj

    # 从数据库中查出一条模型管理器对象所在的模型类数据
    def get_one_object(self, **filters):

        try:
            obj = self.get(**filters)
            print("try")
        except self.model.DoesNotExist:
            print("except")
            obj = None
        return obj

    def get_object_list(self, filters={}, exclude_filters={}, order_by=('-pk',), page_index=None, page_size=None):
        """

        :param filters:所有的过滤参数
        :param exclude_filters: 排除查出的参数
        :param order_by:排序(默认主键从大到小)
        :param page_index:页码
        :param page_size:每页的数目
        :return:
        """
        # 根据条件获取查询集
        obj_queryset = self.filter(**filters).exclude(**exclude_filters).order_by(*order_by)

        # 对查询结果集进行限制
        #if page_index is not None and page_size is not None:
        if all(map(lambda x:x is not None, (page_index, page_size))):
            start = (page_index-1)*page_size
            end = start + page_size
            obj_queryset = obj_queryset[start:end]

        return obj_queryset