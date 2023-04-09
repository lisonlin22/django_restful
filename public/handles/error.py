#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   Error.py
@Time    :   2023/04/09 14:42:06
@Author  :   Lison LIN 
@Version :   1.0
@Contact :   lisonlin22@gmail.com
@Desc    :   
@Wiki    :   
"""

from rest_framework.views import exception_handler
from rest_framework.response import Response


def CustomExceptionHandler(exc, context):
    response = exception_handler(exc, context)
    if response is not None:
        try:
            response.data["code"] = response.status_code
            response.data["msg"] = response.data["detail"]
            response.data["data"] = []
            del response.data["detail"]
        except:
            response = Response(
                {
                    "code": 403,
                    "msg": "内部错误！",
                    "data": [],
                }
            )

    return response
