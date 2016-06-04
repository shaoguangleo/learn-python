#!/usr/bin/env python
# -*- coding=utf-8 -*-


def judge(seq,aset):
    for c in seq:
        if c in aset:
            return True
    return False


import itertools
def judge_v2(seq,aset):
    for item in itertools.ifilter(aset.__contains__,seq):
        return True
    return False


def judge_v3(seq,aset):
    return bool(set(aset).intersection(seq))
