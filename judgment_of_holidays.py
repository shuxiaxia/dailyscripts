#!/usr/bin/env python
# -*- coding: utf-8 -*-
# =============================================================================
# FileName: judgment_of_holidays.py
#     Date: 2017/08/31 13.00
# =============================================================================

from urlparse import urlparse
import urllib
from bs4 import BeautifulSoup
import json
import sys
import os

pwd_dir = sys.path[0]
os.chdir(pwd_dir)

class holiday(object):

    def get_html(self, url):
        '''获取网页源码'''

        html_text = urllib.urlopen(url).read()

        return html_text

    def get_info(self, html_text):
        '''爬取日期相关信息'''
        
        bs =BeautifulSoup(html_text, "html.parser")
        data = bs.find_all('script', {'data-compress': 'off'})
        source = str(data[2])
        source_handle = source.split('\n')[2].strip().split('data: ')[1][:-1]
        dic_info = json.loads(source_handle)
        holiday_list = []
        for i in dic_info['holiday']:
            for j in i['list']:
                holiday_list.append(j)

        info_list = []
        for date in holiday_list:
            if date not in info_list:
                info_list.append(date)
       
        base_dic = {}
        for i in info_list:
          
            year = i['date'].encode('utf-8').split('-')[0]
            month = i['date'].encode('utf-8').split('-')[1]
            day = i['date'].encode('utf-8').split('-')[2]
            if int(month) < 10:
                month = '0' + month
            
            if int(day) < 10:
               day = '0' + day
            holiday_date = year + '-' + month + '-' + day
            
            base_dic[holiday_date] = i['status'].encode('utf-8')

        return base_dic

    def dump_file(self, dumpfile, base_dic):
        '''保存到文件'''

        f = open(dumpfile,"w")
        json.dump(base_dic,f)
        f.close()

if __name__ == '__main__':
    spider = holiday()
    question = "日历"
    count = 1
    url = "http://www.baidu.com/s?wd=" + question + "&rn=" + str(count)
    html_text = spider.get_html(url)
    base_dic = spider.get_info(html_text)
    spider.dump_file('holiday.txt', base_dic)
