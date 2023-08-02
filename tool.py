import json
import logging
import datetime
import time
import random


# 获取日期之差
def getDays(day: str):
    # 获取需要计算的时间戳
    time_array = time.strptime(day, '%Y-%m-%d')
    timestamp = int(time.mktime(time_array))
    # 获取今天的时间戳
    time_array2 = time.strptime(datetime.date.today().__str__(), '%Y-%m-%d')
    timestamp2 = int(time.mktime(time_array2))
    if timestamp2 < timestamp:
        timestamp2, timestamp = timestamp, timestamp2
    # 时间戳相减，然后算出天数
    day = int((timestamp2 - timestamp) / (24 * 60 * 60))
    return day


# 随机颜色
def randomcolor():
    colorArray = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    cardColor = ''
    for i in range(6):
        cardColor += colorArray[random.randint(0, 14)]
    return '#' + cardColor


# 时间戳转换
def ts2time(time: int):
    timeStamp = time
    time_instance = datetime.datetime.fromtimestamp(timeStamp)
    style_time = time_instance.strftime("%Y-%m-%d %H:%M:%S")
    return style_time
