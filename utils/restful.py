#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# 项目名称:XFZ
# 文件名称:restful.py
# 用户名:TQTL
# 创建时间:2018/12/21 13:59


from django.http import JsonResponse


class HttpCode(object):
    """
    HTTP状态码；
    """
    OK = 200
    PARAMS_ERROR = 400
    UN_AUTH = 401
    METHOD_ERROR = 405
    SERVER_ERROR = 500


def result(code=HttpCode.OK, message="", data=None, kwargs=None):
    json_dict = {'code': code, 'message': message, 'data': data}
    if kwargs and isinstance(kwargs, dict) and kwargs.keys():
        json_dict.update(kwargs)
    return JsonResponse(json_dict)


def params_error(message="", data=None):
    return result(code=HttpCode.PARAMS_ERROR, message=message, data=data)


def un_auth(message="", data=None):
    return result(code=HttpCode.UN_AUTH, message=message, data=data)


def method_error(message='', data=None):
    return result(code=HttpCode.METHOD_ERROR, message=message, data=data)


def server_error(message='', data=None):
    return result(code=HttpCode.SERVER_ERROR, message=message, data=data)
