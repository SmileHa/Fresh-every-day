# coding=utf-8
from django.conf.urls import url
from gu_df_user import views


urlpatterns = [
    url(r'^register/$', views.register),  # 展示用户注册页面


]