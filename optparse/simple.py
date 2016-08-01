#!/usr/bin/env python
# coding=utf-8

# Author    :   Guo Shaoguang
# Email     :   sgguo@shao.ac.cn
# Institute :   Shanghai Astronomical Observatory

from optparse import OptionParser

parser = OptionParser()

parser.add_option('-f','--filename',dest='filename',help='write report to FILE',metavar='FILE')

