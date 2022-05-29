# -*- coding: utf-8 -*-
#简单txt转html
import os,sys

file1 = sys.argv[1]
outfile = sys.argv[1]

filename = open(file1,'r') 
with open(outfile+'.html','w') as e:
	for line in filename.readlines():
		e.write("<pre>" + line + "</pre>")

