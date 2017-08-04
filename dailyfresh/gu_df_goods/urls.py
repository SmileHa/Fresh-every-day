# coding=utf-8
from django.conf.urls import url

from gu_df_goods import views

urlpatterns = [
    url(r'^$', views.home_list_page),  # 显示首页内容
]