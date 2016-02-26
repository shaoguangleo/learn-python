# -*- coding: UTF-8 -*-

filepath='data.txt'

f = open(filepath, 'r')
content=""
try:
    while True:
        chunk = f.read(8)
        print chunk
        if not chunk:
            break
        content+=chunk
finally:
    f.close()
#    print content