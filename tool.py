import json
import logging
import datetime
import time
import random


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


def randomcolor():
    colorArray = ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    cardColor = ''
    for i in range(6):
        cardColor += colorArray[random.randint(0, 14)]
    return '#' + cardColor
