# !/usr/bin/env python
# -*- coding:utf-8 -*-
# support: linliangsuan@qq.com
from rest_framework.renderers import JSONRenderer
class format_json(JSONRenderer):
    charset = 'utf-8'
    format = 'json'