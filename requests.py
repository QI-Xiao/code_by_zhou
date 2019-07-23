# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 'author':'zouliwei'


from werkzeug.wrappers import Request


class BaseRequest(Request):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 为请求对象增加一个字典以供在多次处理同一请求对象时共享数据
        self.storage = dict()
