# coding=utf-8
from django.conf.urls import url
from gu_df_cart import views
urlpatterns = [
    url(r'^add/', views.cart_add),  # 向购物车中添加信息
    url(r'^count/', views.cart_count),  # 获取用户购物车中商品的数目
    url(r'^$', views.cart_show),  # 显示购物车界面
]