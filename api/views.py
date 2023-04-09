#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   views.py
@Time    :   2023/04/09 14:46:17
@Author  :   Lison LIN 
@Version :   1.0
@Contact :   lisonlin22@gmail.com
@Desc    :   
@Wiki    :   
"""

from public.serializers.api import EnvSerializers
from public.filters.api import EnvFilter
from public.serializers.model_viewset import ModelViewSetStyle
from api.models import Env


class EnvView(ModelViewSetStyle):
    """学生列表数据接口"""

    queryset = Env.objects.all().order_by("-id")
    serializer_class = EnvSerializers
    filterset_class = EnvFilter
    search_fields = [
        "env_name",
    ]

    def get_queryset(self):
        return super().get_queryset()
