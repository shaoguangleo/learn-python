# -*- coding: UTF-8 -*-

filepath='data.txt'

f = open(filepath, 'r')
content = ''

with open(filepath,'r') as f:
    content = f.readlines()

for i in content:
    print '>' + i,
