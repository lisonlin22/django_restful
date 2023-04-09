#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   api.py
@Time    :   2023/04/09 14:45:04
@Author  :   Lison LIN 
@Version :   1.0
@Contact :   lisonlin22@gmail.com
@Desc    :   api 应用的过滤器
@Wiki    :   
"""

from django_filters import rest_framework as filters
from api.models import *


class EnvFilter(filters.FilterSet):
    """学生列表过滤器"""

    class Meta:
        model = Env
        fields = "__all__"
