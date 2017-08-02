from django.shortcuts import render

# Create your views here.


# 注册界面
def register(request):
    return render(request, 'register.html')