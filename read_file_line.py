# -*- coding: UTF-8 -*-

filepath='data.txt'

f = open(filepath, 'r')
content = ''

try:
	while True:
		line = f.readline()
		print '>>>'
		print line
		if not line:
			break
		content += line
finally:
	f.close()