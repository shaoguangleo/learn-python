#!/usr/bin/env python
# coding=utf-8

# Author    :   Guo Shaoguang
# Email     :   sgguo@shao.ac.cn
# Institute :   Shanghai Astronomical Observatory

import numpy as np

print 'The usage of hypot'

print 'Given the legs of a right triangle, return its hypotenuse'

xarr=3*np.ones((3,3))
yarr=4*np.ones((3,3))
zarr = np.hypot(xarr,yarr)

print zarr
