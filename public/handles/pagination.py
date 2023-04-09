#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@File    :   Pagination.py
@Time    :   2023/04/09 14:32:44
@Author  :   Lison LIN 
@Version :   1.0
@Contact :   lisonlin22@gmail.com
@Desc    :   处理分页
@Wiki    :   
"""
from rest_framework.pagination import PageNumberPagination, OrderedDict
from rest_framework.response import Response


class Pagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "size"
    page_query_param = "page"
    max_page_size = 1000

    def get_results(self, data):
        return data["data"]

    def get_paginated_response(self, data):
        return Response(
            OrderedDict(
                [
                    ("count", self.page.paginator.count),
                    ("data", data),
                    ("code", 0),
                    ("msg", ""),
                    ("request_id", self.request.id),
                ]
            )
        )
