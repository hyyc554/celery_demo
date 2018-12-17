from __future__ import absolute_import, unicode_literals

from celery import shared_task
from celery_demo.celery import app
import time
import json
import redis

pool = redis.ConnectionPool(host='192.168.0.2', port=6379, password='hyc554', max_connections=1000)
conn = redis.Redis(connection_pool=pool)



@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@app.task
def fence(*args):
    """
    一个简单的电子围栏demo
    :param numbers:
    :return:
    """
    # count = 0
    # while count<10:
    #     conn.hset('celery','hyc%s'%count,123)
    #
    #     # print('123')
    #     count+=1
    print("我每隔5秒钟时间执行一次....")

    return 123456789

    # return int(time.time())



@app.task
def myadd(*args):
    """
    一个简单的电子围栏demo
    :param numbers:
    :return:
    """
    count = 0
    conn.hset('hyyy213c','hyc',19921225)
    count+=1
    print("我每隔5秒钟时间执行一次....")
