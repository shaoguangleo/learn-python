#!/usr/bin/env python
# coding=utf-8

# Author    :   Guo Shaoguang
# Email     :   sgguo@shao.ac.cn
# Institute :   Shanghai Astronomical Observatory

print 'The use cases of format function'

print
print '{0} {1}'.format('hello',2016)
print '{1} {0} {1}'.format('hello',2016)

print
print '{name},{age}'.format(age=18,name='leo')

leo = ['leo',18]
print '{0[0]},{0[1]}'.format(leo)

print
print '{:^8}'.format(123)
print '{:<8}'.format(123)
print '{:>8}'.format(123)
print '{:a>8}'.format(123)

print
print '{:.2f}'.format(123.456)

print 
print '{:b}'.format(10)
print '{:d}'.format(10)
print '{:o}'.format(10)
print '{:x}'.format(10)

print
print '{:,}'.format(1234567890)
