#!/usr/bin/env python
# -*- coding=utf8 -*-

def read_file_by_chunks(filename,chunksize = 102):
    file_obj = open(filename,'rb')
    while True:
        chunk = file_obj.read(chunksize)
        if not chunk:
            break
        yield chunk
    file_obj.close()

'''
    # sample
    for chunk in read_file_by_chunks('filename'):
        do_something_with(chunk)
'''