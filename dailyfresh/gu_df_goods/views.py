# coding=utf-8
from django.shortcuts import render
from gu_df_goods.models import Goods
from gu_df_goods.enums import *
# Create your views here.


def home_list_page(request):
    fruits_new = Goods.objects_logic.get_goods_list_by_type(goods_type_id=FRUITS, limit=3, sort='new')
    fruits = Goods.objects_logic.get_goods_list_by_type(goods_type_id=FRUITS, limit=4)
    seafood_new = Goods.objects_logic.get_goods_list_by_type(goods_type_id=SEAFOOD, limit=3, sort='new')
    seafood = Goods.objects_logic.get_goods_list_by_type(goods_type_id=SEAFOOD, limit=4)
    meat_new = Goods.objects_logic.get_goods_list_by_type(goods_type_id=MEAT, limit=3, sort='new')
    meat = Goods.objects_logic.get_goods_list_by_type(goods_type_id=MEAT, limit=4)
    eggs_new = Goods.objects_logic.get_goods_list_by_type(goods_type_id=EGGS, limit=3, sort='new')
    eggs = Goods.objects_logic.get_goods_list_by_type(goods_type_id=EGGS, limit=4)
    vegetables_new = Goods.objects_logic.get_goods_list_by_type(goods_type_id=VEGETABLES, limit=3, sort='new')
    vegetables = Goods.objects_logic.get_goods_list_by_type(goods_type_id=VEGETABLES, limit=4)
    frozen_new = Goods.objects_logic.get_goods_list_by_type(goods_type_id=FROZEN, limit=3, sort='new')
    frozen = Goods.objects_logic.get_goods_list_by_type(goods_type_id=FROZEN, limit=4)

    # 组织模板上下文
    context = {'fruits_new': fruits_new, 'fruits': fruits,
               'seafood_new': seafood_new, 'seafood': seafood,
               'meat_new': meat_new, 'meat': meat,
               'eggs_new': eggs_new, 'eggs': eggs,
               'vegetables_new': vegetables_new, 'vegetables': vegetables,
               'frozen_new': frozen_new, 'frozen': frozen}

    return render(request, 'index.html', context)