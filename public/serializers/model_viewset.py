#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   ModelViewSet.py
@Time    :   2023/04/09 14:30:50
@Author  :   Lison LIN 
@Version :   1.0
@Contact :   lisonlin22@gmail.com
@Desc    :   模型序列化
@Wiki    :   
"""

from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from public.handles.format_json import FormatJson
from public.handles.pagination import Pagination
from public.permission.model import CheckUserModelPermissions


class ModelViewSetStyle(ModelViewSet):
    filter_backends = [DjangoFilterBackend, SearchFilter]
    permission_classes = [
        CheckUserModelPermissions,
    ]
    pagination_class = Pagination
    renderer_classes = (FormatJson,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if isinstance(request.data, list):
            serializer = self.get_serializer(data=request.data, many=True)
        valid = serializer.is_valid(raise_exception=False)
        if not valid:
            return Response(
                {
                    "code": 1,
                    "msg": "创建失败！",
                    "data": [],
                    "request_id": request.id,
                }
            )
        self.perform_create(serializer)
        return Response({"code": 0, "msg": "添加成功！", "data": serializer.data})

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {
                "code": 0,
                "msg": "删除成功！",
                "data": [],
                "request_id": request.id,
            }
        )

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop("partial", False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        valid = serializer.is_valid(raise_exception=False)
        if not valid:
            return Response(
                {
                    "code": 1,
                    "msg": "更新失败!",
                    "data": [],
                    "request_id": request.id,
                }
            )
        self.perform_update(serializer)
        if getattr(instance, "_prefetched_objects_cache", None):
            instance._prefetched_objects_cache = {}
        return Response({"code": 0, "msg": "更新成功!", "data": serializer.data})

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(
            {
                "code": 0,
                "msg": "",
                "data": serializer.data,
                "request_id": request.id,
            }
        )
