#!/usr/bin/env python
# -*- coding: utf-8 -*-
# =============================================================================
# FileName: holiday_status.py
#     Date: 2017/08/31 13.00
#   Author: 王晓磊
#    Email: 15835826467@163.com
# =============================================================================

import json
import sys
import os
import time

pwd_dir = sys.path[0]
os.chdir(pwd_dir)

def load_file():
    holiday_file = open("holiday.txt")
    base_dic = json.load(holiday_file)
    holiday_file.close()
 
    return base_dic

def judgment(datestr, base_dic): 
    '''返回状态码'''

    if datestr in base_dic.keys():
        return base_dic[datestr]
    else:
        return 3

def main(datestr):
    base_dic = load_file()
    status_code = judgment(datestr, base_dic)
   
    return status_code

def usage():
    return  "Usage:\neg: holiday_status.main('2017-10-01')\n返回 1 表示当天为节假日\n返回 2 表示当天为调休上班\n返回 3 表示正常日期"
    

if __name__ == '__main__':
    current_time = time.strftime("%Y-%m-%d",time.localtime())
    print "当前日期为", current_time
    print main(current_time)
    print usage()
    
