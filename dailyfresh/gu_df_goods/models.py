# coding=utf-8

from django.db import models
from gu_db.base_model import BaseModel
from gu_db.base_manager import BaseModelManager
from tinymce.models import HTMLField
from gu_df_goods.enums import *


#  商品模型逻辑管理类
class GoodsLogicManger(BaseModelManager):

    # 根据商品类型查询商品信息:包含商品图片路径
    def get_goods_list_by_type(self, goods_type_id, limit=None, sort='default'):

        # 首先调用GoodsManger的get_goods_list_by_type方法获取商品信息
        goods_list = Goods.objects.get_goods_list_by_type(goods_type_id=goods_type_id, limit=limit, sort=sort)
        for goods in goods_list:
            # 查询出商品的图片
            img = Image.objects.get_image_by_goods_id(goods_id=goods.id)
            # 给商品加一个属性img_url, 记录商品图片路径
            goods.img_url = img.img_url
        return goods_list


# 商品管理类
class GoodsManager(BaseModelManager):
    # 根据商品类型查询商品信息
    def get_goods_list_by_type(self, goods_type_id, limit=None, sort='default'):

        if sort == 'new':
            # 查询新品
            goods_list = self.get_object_list(filters={'goods_type_id': goods_type_id}, order_by=('-create_time',))
        elif sort == 'price':
            # 根据价格来查商品
            goods_list = self.get_object_list(filters={'goods_type_id':goods_type_id}, order_by=('goods_price',))
        elif sort == 'hot':
            # 根据人气来查商品
            goods_list = self.get_object_list(filters={'goods_type_id':goods_type_id}, order_by=('-goods_sales',))
        else:
            # 按照默认方式查询商品
            goods_list = self.get_object_list(filters={'goods_type_id':goods_type_id})

        if limit:
            goods_list = goods_list[:limit]
        return goods_list


# 商品类
class Goods(BaseModel):
    goods_type_choice = (
        (FRUITS, GOODS_TYPE[FRUITS]),
        (SEAFOOD, GOODS_TYPE[SEAFOOD]),
        (MEAT, GOODS_TYPE[MEAT]),
        (EGGS, GOODS_TYPE[EGGS]),
        (VEGETABLES, GOODS_TYPE[VEGETABLES]),
        (FROZEN, GOODS_TYPE[FROZEN]),
    )

    goods_type_choic = ((k, v) for k, v in GOODS_TYPE.items())
    goods_type_id = models.SmallIntegerField(choices=goods_type_choic, help_text='商品种类')

    goods_name = models.CharField(max_length=32, help_text='商品名称')
    goods_sub_title = models.CharField(max_length=128, help_text='商品副标题')
    goods_price = models.DecimalField(max_digits=10, decimal_places=2, help_text='商品价格')
    goods_ex_price = models.DecimalField(max_digits=10, decimal_places=2, help_text='商品运费')
    goods_unite = models.CharField(max_length=16, default='500g', help_text='商品单位')
    goods_info = HTMLField(help_text='商品描述')
    goods_stock = models.IntegerField(default=1, help_text='商品库存')
    # 0.商品上线　１：商品下线
    goods_status = models.SmallIntegerField(default=0, help_text='商品状态')
    goods_sales = models.IntegerField(default=0, help_text='商品销量')

    # 商品图片类

    objects = GoodsManager()
    objects_logic = GoodsLogicManger()

    class Meta:
        db_table = 's_goods'


# 商品图片模型管理类
class ImageManger(BaseModelManager):

    def get_image_by_goods_id(self, goods_id):
        # 根据商品id获取商品图片
        img = self.get_object_list(filters={'goods_id':goods_id})[0]
        return img


#  商品图片类
class Image(BaseModel):

    goods = models.ForeignKey('Goods', help_text='所属商品')
    img_url = models.ImageField(upload_to='goods', help_text='图片路径')
    is_def = models.BooleanField(default=False, help_text='是否默认')

    objects = ImageManger()

    class Meta:
        db_table = 's_goods_image'