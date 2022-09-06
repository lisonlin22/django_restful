# !/usr/bin/env python
# -*- coding:utf-8 -*-
# support: linliangsuan@qq.com
# 处理异常访问
from rest_framework.views import exception_handler
from rest_framework.response import Response

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)
    if response is not None:
        try:
            response.data['code'] = 1
            response.data['msg'] = response.data['detail']
            response.data['data'] = []
            del response.data['detail']
        except:
            response = Response({
                "code" : 403,
                "msg" : "内部错误！",
                "data": [],
            })

    return response