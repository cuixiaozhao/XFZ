#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# 项目名称:XFZ
# 文件名称:urls.py
# 用户名:TQTL
# 创建时间:2018/12/21 12:03
from django.urls import path
from . import views

app_name = 'xfzauth'
urlpatterns = [
    path('login/', views.login_view, name='login')
]
