#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   models.py
@Time    :   2023/04/09 14:22:40
@Author  :   Lison LIN 
@Version :   1.0
@Contact :   lisonlin22@gmail.com
@Desc    :   
@Wiki    :   
"""

from django.db import models


class Env(models.Model):
    """
    @description  : 环境
    @param    :
    @Returns  :
    @Wiki     :
    """

    env_name = models.CharField(max_length=20, verbose_name="环境名称")
    env_name_zh = models.CharField(
        max_length=50, verbose_name="环境名称", null=True, blank=True
    )
