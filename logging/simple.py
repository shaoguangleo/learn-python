#!/usr/bin/env python
# coding=utf-8

# Author    :   Guo Shaoguang
# Email     :   sgguo@shao.ac.cn
# Institute :   Shanghai Astronomical Observatory

import logging
import sys

logger = logging.getLogger('LOG-TEST')

formatter = logging.Formatter('%(name)-12s %(asctime)s %(levelname)-8s %(message)s','%a, %d %b %Y %H:%M:%S',)
file_handler = logging.FileHandler('test.log')
file_handler.setFormatter(formatter)

stream_handler = logging.StreamHandler(sys.stderr)

logger.addHandler(file_handler)
logger.addHandler(stream_handler)

logger.setLevel(logging.ERROR)

logger.error('ERROR-OUTPUT')
logger.removeHandler(stream_handler)
logger.error('ERROR-OUTPUT')
