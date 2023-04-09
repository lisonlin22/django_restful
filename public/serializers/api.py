#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   api.py
@Time    :   2023/04/09 14:43:57
@Author  :   Lison LIN 
@Version :   1.0
@Contact :   lisonlin22@gmail.com
@Desc    :   API 应用的序列化
@Wiki    :   
"""

from rest_framework import serializers
from api.models import *


class EnvSerializers(serializers.ModelSerializer):
    """环境"""

    class Meta:
        model = Env
        fields = "__all__"
