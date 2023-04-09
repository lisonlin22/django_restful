#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   format_json.py
@Time    :   2023/04/09 14:35:43
@Author  :   Lison LIN 
@Version :   1.0
@Contact :   lisonlin22@gmail.com
@Desc    :   
@Wiki    :   
"""

# !/usr/bin/env python
# -*- coding:utf-8 -*-
# support: linliangsuan@qq.com
from rest_framework.renderers import JSONRenderer


class FormatJson(JSONRenderer):
    charset = "utf-8"
    format = "json"
