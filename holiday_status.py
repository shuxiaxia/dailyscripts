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
import datetime

pwd_dir = sys.path[0]
os.chdir(pwd_dir)

def load_file():
    holiday_file = open("holiday.txt")
    base_dic = json.load(holiday_file)
    holiday_file.close()
 
    return base_dic

def judgment(datestr, base_dic): 
    '''返回状态码'''

    week = datetime.datetime.strptime(datestr, '%Y-%m-%d').weekday()
    if datestr in base_dic.keys():
        if base_dic[datestr] == "1":
            return 0
        else:
            return 1
    else:
        if week in [5, 6]:
            return 0
        else:
            return 1
     

def main(datestr):
    base_dic = load_file()
    status_code = judgment(datestr, base_dic)
   
    return status_code

def usage():
    return  "Usage:\neg: holiday_status.main('2017-10-01')\n返回 0 表示当天为休息日\n返回 1 表示当天为工作日"
    

if __name__ == '__main__':
    current_time = datetime.datetime.now().strftime('%Y-%m-%d')
    #print "当前日期为", current_time
    print current_time, main(current_time)
    print "2017-09-09", main('2017-09-09')
    print "2017-09-30", main('2017-09-30')
    print "2017-10-01", main('2017-10-01')
    print "2017-10-08", main('2017-10-08')
    print usage()
    
