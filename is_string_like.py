#!/usr/bin/env python
# -*- coding=utf-8 -*-

def is_string_like(obj):
    try:
        obj + ' '
    except:
        return False
    else:
        return True