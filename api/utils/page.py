# !/usr/bin/env python
# -*- coding:utf-8 -*-
# support: linliangsuan@qq.com
# 分页器
from rest_framework.pagination import PageNumberPagination, OrderedDict
from rest_framework.response import Response

class page(PageNumberPagination):
    page_size = 10000000
    page_size_query_param = 'size'
    page_query_param = "page"
    max_page_size = 10000000
    def get_results(self, data):
        return data['data']
    def get_paginated_response(self, data):
        return Response(OrderedDict([
            # ('count', self.page.paginator.count),
            ('data', data),
            ('code', 0),
            ('msg', ''),
        ]))

