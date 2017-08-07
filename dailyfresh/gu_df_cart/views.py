# coding=utf-8
from django.shortcuts import render
from django.views.decorators.http import require_GET,require_POST,require_http_methods
from django.http import JsonResponse
from gu_df_goods.models import Goods
from gu_df_cart.models import Cart, CartManger
from utils.deacrators import login_required


@require_GET
@login_required
def cart_add(request):
    goods_id = request.GET.get('goods_id')
    goods_count = request.GET.get('goods_count')
    passport_id = request.session.get('passport_id')
    goods = Goods.objects.get_goods_by_id(goods_id=goods_id)
    if int(goods_count) > goods.goods_stock:
        return JsonResponse({'res': 0})
    else:
        Cart.objects.add_one_cart_info(passport_id=passport_id, goods_id=goods_id, goods_count=int(goods_count))
        return JsonResponse({'res': 1})


# 获取用户购物车中商品的数目
@require_GET
@login_required
def cart_count(request):

    passport_id = request.session.get('passport_id')
    #  根据用户id查找用户购物车中商品的数量
    goods_count = Cart.objects.get_cart_count_by_passport(passport_id=passport_id)
    return JsonResponse({'res': goods_count})


@login_required
def cart_show(request):

    passport_id = request.session.get('passport_id')
    cart_list = Cart.objects_logic.get_cart_list_by_passport(passport_id=passport_id)
    goods_count = Cart.objects.get_cart_count_by_passport(passport_id=passport_id)

    return render(request, 'cart.html', {'cart_list': cart_list, 'goods_count': goods_count})









