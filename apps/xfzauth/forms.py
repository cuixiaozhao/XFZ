#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# 项目名称:XFZ
# 文件名称:forms.py
# 用户名:TQTL
# 创建时间:2018/12/21 11:39
from django import forms
from apps.forms import FormMixin


class LoginForm(forms.Form, FormMixin):
    telephone = forms.CharField(max_length=11)
    password = forms.CharField(max_length=10, min_length=6,
                               error_messages={'max_length': '密码最多不能超过20个字符！', 'min_length': '密码最少不能少于6个字符！'})
    remember = forms.IntegerField(required=False)
