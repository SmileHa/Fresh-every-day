# coding=utf-8
from django.shortcuts import render
from gu_df_user.models import Passport
# Create your views here.


# 注册界面
def register(request):

    return render(request, 'register.html')


def register_handle(request):
    # 接收用户注册的信息
    username = request.POST.get('user_name')
    password = request.POST.get('pwd')
    email = request.POST.get('email')

    
