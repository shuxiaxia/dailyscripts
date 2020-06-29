#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# FileName: customlog.py
#     Date: 2017/08/08 10:00
# =============================================================================
import logging
import logging.handlers
     
class Logger():
    def __init__(self, tag="log", filename="python.log"):
        self.__logger = logging.getLogger(tag)
          
        # 防止重复记录日志的问题
        if not self.__logger.handlers:

            formatter = logging.Formatter('%(asctime)s %(name)s [%(levelname)s] "%(message)s"')
            self.__logger.setLevel(logging.DEBUG)
  
            fh = logging.FileHandler(filename)
            fh.setLevel(logging.DEBUG)
            fh.setFormatter(formatter)
            self.__logger.addHandler(fh)
              
    def getlogger(self):
        return self.__logger
  
          
def main():
    print ("python logger")
  
      
if __name__ == "__main__":
    main()
