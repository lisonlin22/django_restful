# !/usr/bin/env python
# -*- coding:utf-8 -*-
# support: linliangsuan@qq.com
# 序列化
from rest_framework import serializers
from api.models import *

class student_serializer(serializers.ModelSerializer):
    """学生列表序列化"""
    class Meta:
        model = student
        fields = "__all__"

class achievement_serializer(serializers.ModelSerializer):
    """学生列表序列化"""
    student_name = serializers.CharField(source="student.student_name", read_only=True)
    student_number = serializers.CharField(source="student.student_number", read_only=True)
    class Meta:
        model = achievement
        fields = "__all__"


