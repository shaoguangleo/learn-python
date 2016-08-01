#!/usr/bin/env python
# coding=utf-8

# Author    :   Guo Shaoguang
# Email     :   sgguo@shao.ac.cn
# Institute :   Shanghai Astronomical Observatory

from optparse import OptionParser

parser = OptionParser()

parser.add_option('-f','--filename',dest='filename',help='write report to FILE',metavar='FILE')
parser.add_option('-q','--quiet',action='store_false',dest='verbose',default=True,help='don\'t print status messages to stdout')

(options,args) = parser.parse_args()

