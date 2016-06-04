#!/usr/bin/env python
# -*- coding=utf8 -*-

def reindent(s,num_spaces):
    leading_space = num_spaces * ' '

    lines = [ leading_space + line.strip() for line in s.splitlines() ]

    return '\n'.join(lines)