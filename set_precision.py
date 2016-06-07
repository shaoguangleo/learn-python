#!/usr/bin/env python
# -*- coding=utf8 -*-

import decimal

def set_precision(cnt):
    decimal.getcontext().prec = cnt
