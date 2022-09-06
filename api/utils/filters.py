# !/usr/bin/env python
# -*- coding:utf-8 -*-
# support: linliangsuan@qq.com
# 过滤器
from django_filters import rest_framework as filters
from api.models import *

class student_filter(filters.FilterSet):
    """学生列表过滤器"""
    class Meta:
        model = student
        fields = "__all__"

class achievement_filter(filters.FilterSet):
    """学生列表序列化"""
    student_name = filters.CharFilter(field_name='student__student_name', lookup_expr='exact')
    class Meta:
        model = achievement
        fields = "__all__"

