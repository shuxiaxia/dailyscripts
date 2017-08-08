#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# FileName: file_compare_html.py
#     Date: 2017/08/08 10:00
#   Author: 王晓磊
#    Email: 15835826467@163.com
# =============================================================================
import difflib
import sys

try:
    textfile1 = sys.argv[1]
    textfile2 = sys.argv[2]
except Exception as e:
    print ("Error:" +str(e)) 
    print ("Usage: file_compare filename1 fielname2")
    sys.exit()

def readfile(filename):
    try:
        fileHandle = open(filename, 'rb')
        text = fileHandle.read().splitlines()
        fileHandle.close()
        return text
    except IOError as error:
        print ("Read file Error:" +str(error))
        sys.exit()

if textfile1 == "" or textfile2 == "":
    print ("Usage: file_compare filename1 fielname2")
    sys.exit()

text1_lines = readfile(textfile1)
for i in range(0, len(text1_lines)):
    text1_lines[i] = bytes(text1_lines[i]).decode('ascii')

text2_lines = readfile(textfile2)
for i in range(0, len(text2_lines)):
    text2_lines[i] = bytes(text2_lines[i]).decode('ascii')

d = difflib.HtmlDiff()
print (d.make_file(text1_lines, text2_lines))
