#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   auth.py
@Time    :   2023/04/09 14:31:05
@Author  :   Lison LIN 
@Version :   1.0
@Contact :   lisonlin22@gmail.com
@Desc    :   
@Wiki    :   
"""

# !/usr/bin/env python
# -*- coding:utf-8 -*-
# by linliangsuan@ghuawei.com
import datetime
from django.contrib.auth.models import User
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from public.handles.format_json import FormatJson


EXPIRE_MINUTES = getattr(settings, "REST_FRAMEWORK_TOKEN_EXPIRE_MINUTES", 1)


class Login(ObtainAuthToken):
    """Create user token"""

    renderer_classes = (FormatJson,)

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data["user"]
            token, created = Token.objects.get_or_create(user=user)
            user_info = User.objects.filter(username=user).values(
                "username", "is_active", "last_login", "email", "date_joined"
            )
            time_now = datetime.datetime.now()
            if created or token.created < time_now - datetime.timedelta(
                minutes=EXPIRE_MINUTES
            ):
                token.delete()
                token = Token.objects.create(user=serializer.validated_data["user"])
                token.created = time_now
                token.save()

            return Response(
                {
                    "data": {"token": token.key, "user": user_info[0]},
                    "code": status.HTTP_200_OK,
                    "msg": "",
                    "requset_id": request.id,
                }
            )
        return Response(
            {
                "data": "",
                "code": status.HTTP_401_UNAUTHORIZED,
                "msg": "认证失败！",
                "requset_id": request.id,
            }
        )
