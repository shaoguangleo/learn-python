#!/usr/bin/env python
# coding=utf-8

# Author    :   Guo Shaoguang
# Email     :   sgguo@shao.ac.cn
# Institute :   Shanghai Astronomical Observatory

import logging
import sys

logging.basicConfig(level=logging.INFO,
                    format = 'levelname:%(levelname)s filename: %(filename)s '
                    'outputNumber: [%(lineno)d thread: %(threadName)s output msg: %(message)s]'
                    ' - %(asctime)s',datefmt='%a, %d %b %Y %H:%M:%S',
                   filename = 'loggmsg.log')

logging.error('error...')
logging.info('info...')
logging.warning('warning...')
