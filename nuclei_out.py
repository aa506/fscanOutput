# -*- coding: utf-8 -*-
#简单txt转html
import os,sys

file1 = sys.argv[1]
outfile = sys.argv[1]

filename = open(file1,'r') #后续弄成参数传递
with open(outfile+'.html','w') as e:
	for line in filename.readlines():
		# if ' ' in line:
		# 	line = '<td><tr>'+line+ '</td></tr>'
		e.write("<pre>" + line + "</pre>")

