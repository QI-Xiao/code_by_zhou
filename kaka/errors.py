# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 'author':'zouliwei'


class Error(Exception):
    pass


class HTMLRenderError(Error):
    pass


class ReverseURLFailedError(Error):
    pass


class RestResponserHandlerError(Error):
    pass
