#!/usr/bin/env python
# -*- coding: utf-8 -*-
# =============================================================================
# FileName: time_range.py
#     Date: 2017/09/07 10:00
# =============================================================================


import time
import datetime


def alert_range(current_timestamp, start, stop):
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    start_time = datetime.datetime.strptime(today + " " +start, "%Y-%m-%d %H")
    stop_time = datetime.datetime.strptime(today + " " +stop, "%Y-%m-%d %H")


    start_timestamp = int(time.mktime(start_time.timetuple()))
    stop_timestamp = int(time.mktime(stop_time.timetuple()))

    if current_timestamp >= start_timestamp and current_timestamp <= stop_timestamp:
        return 0
    else:
        return 1


current_timestamp = int(time.time())
print(alert_range(current_timestamp, '00', '08'))
