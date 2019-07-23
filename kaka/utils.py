# !/usr/bin/env python
# -*- coding: utf-8 -*-
# 'author':'zouliwei'


from werkzeug.routing import redirect as werkzeug_redirect

from .responses import BaseResponse


def redirect(location, code=302):
    return werkzeug_redirect(location, code, BaseResponse)

