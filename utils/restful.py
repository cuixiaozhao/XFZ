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
    """
    定义返回结果！
    :param code:
    :param message:
    :param data:
    :param kwargs:
    :return:
    """
    json_dict = {'code': code, 'message': message, 'data': data}
    if kwargs and isinstance(kwargs, dict) and kwargs.keys():
        json_dict.update(kwargs)
    return JsonResponse(json_dict)


def ok():
    """
    返回值状态OK，即HTTP状态码200；
    :return:
    """
    return result()


def params_error(message="", data=None):
    """
    参数错误,HTTP状态码400；
    :param message:
    :param data:
    :return:
    """
    return result(code=HttpCode.PARAMS_ERROR, message=message, data=data)


def un_auth(message="", data=None):
    """
    未认证的，HTTP状态码401；
    :param message:
    :param data:
    :return:
    """
    return result(code=HttpCode.UN_AUTH, message=message, data=data)


def method_error(message='', data=None):
    """
    方法错误，HTTP状态码405；
    :param message:
    :param data:
    :return:
    """
    return result(code=HttpCode.METHOD_ERROR, message=message, data=data)


def server_error(message='', data=None):
    """
    服务端错误，HTTP状态码5xx；
    :param message:
    :param data:
    :return:
    """
    return result(code=HttpCode.SERVER_ERROR, message=message, data=data)
