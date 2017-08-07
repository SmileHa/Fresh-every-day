# coding=utf-8

from django.db import models
from gu_db.base_model import BaseModel
from gu_db.base_manager import BaseModelManager
from gu_df_user.views import Passport
from django.db.models import Sum
from gu_df_goods.models import Image


# 购物车模型管理类(获取图片)
class CartLogicManger(BaseModelManager):

    def get_cart_list_by_passport(self, passport_id):
        cart_list = Cart.objects.get_cart_list_by_passport(passport_id=passport_id)
        print(cart_list.count())
        for cart_info in cart_list:
            # 查询图片路径
            img = Image.objects.get_image_by_goods_id(goods_id=cart_info.goods.id)
            cart_info.goods.img_url = img.img_url
            #print('img_url%s'%img.img_url)
        return cart_list


# 购物车管理类
class CartManger(BaseModelManager):

    # 根据用户id和商品id查询用户购物信息
    def get_one_cart_info(self, passport_id, goods_id):
        cart_info = self.get_one_object(passport_id=passport_id, goods_id=goods_id)
        return cart_info

    # 添加一条商品信息
    def add_one_cart_info(self, passport_id, goods_id, goods_count):
        # 判断购物车中是否已经有该商品信息
        cart_info = self.get_one_cart_info(passport_id=passport_id, goods_id=goods_id)
        # 有  则更新购物车中商品的数量
        if cart_info:
            cart_info.goods_count = cart_info.goods_count + goods_count
            cart_info.save()
        # 无  则添加商品
        else:
            cart_info = self.create_one_object(passport_id=passport_id, goods_id=goods_id, goods_count=goods_count)
        return cart_info

    # 查询用户购物车中商品的数量  根据passpord_id
    def get_cart_count_by_passport(self, passport_id):
        goods_count_dict = self.get_object_list(filters={'passport_id': passport_id}).aggregate(Sum('goods_count'))
        return goods_count_dict['goods_count__sum']

    # 查询用户购物车信息
    def get_cart_list_by_passport(self, passport_id):

        cart_list = self.get_object_list(filters={'passport_id': passport_id})

        return cart_list


# 购物车类
class Cart(BaseModel):
    passport = models.ForeignKey('gu_df_user.Passport', help_text='账户')
    goods = models.ForeignKey('gu_df_goods.Goods', help_text='商品')
    goods_count = models.IntegerField(default=1, help_text='商品数量')

    objects = CartManger()
    objects_logic = CartLogicManger()

    class Meta:
        db_table = 's_cart'
