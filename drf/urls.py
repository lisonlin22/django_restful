#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   urls.py
@Time    :   2023/04/09 14:18:44
@Author  :   Lison LIN 
@Version :   1.0
@Contact :   lisonlin22@gmail.com
@Desc    :   
@Wiki    :   
"""

from django.contrib import admin
from django.urls import path
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls")),
]
