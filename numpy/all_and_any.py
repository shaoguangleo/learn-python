#!/usr/bin/env python
# coding=utf-8

# Author    :   Guo Shaoguang
# Email     :   sgguo@shao.ac.cn
# Institute :   Shanghai Astronomical Observatory

import numpy as np

a = np.array([[2, 2, 2, 0, 0, 3], 
           [2, 2, 2, 0, 0, 0], 
           [0, 0, 1, 1, 0, 0],
           [0, 0, 1, 1, 0, 0],
           [0, 0, 0, 0, 1, 0],
           [0, 0, 0, 0, 0, 0]])

b = a.copy()

print ">Check if a equal to b, I mean every components"
print '>Will return True just when every components is same'
print (a == b).all()

c = b.copy()
c[0] = 0
print ">Check if b equal to c, I mean every components"
print '>Will return True just when every components is same'
print (b == c).all()


print ">Check if a not equal to b, I mean every components"
print '>Will return True just when every components is different'
print (a == b).any()

c = b.copy()
c = b + 1
print ">Check if b not equal to c, I mean every components"
print '>Will return True just when every components is different'
print (b == c).any()
