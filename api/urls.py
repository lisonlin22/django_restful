#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   urls.py
@Time    :   2023/04/09 14:49:19
@Author  :   Lison LIN 
@Version :   1.0
@Contact :   lisonlin22@gmail.com
@Desc    :   
@Wiki    :   
"""

from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from api import views
from public.handles.auth import Login

router = DefaultRouter()
router.register(r"env", views.EnvView, basename="env")  # 向路由器中注册视图集

app_name = "api"
urlpatterns = [
    path("login/", Login.as_view(), name="login"),  # 登录认证
]
urlpatterns += router.urls  # 将路由器中的所以路由信息追到到django的路由列表中
