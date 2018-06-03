# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 15:08:21 2018

@author: lenovo
"""

msg={"地址":"山东省泰安市泰山区",
 "手机号码":"18515797767",
 "寄信人":"lyyaocool"}
print(msg["地址"])
print(msg["手机号码"])
print(msg["寄信人"])

zidian={"姓名":"lyyao",
 "身高":"180cm",
 "性别":"male",
 "年龄":"22"}
print(zidian["姓名"])
print(zidian["身高"])
print(zidian["性别"])
print(zidian["年龄"])

xzhq={'name':'',
      'song':'',
      'nicheng':'',
      '认识女朋友':''}
songs=xzhq['songs']
print(songs)
print("歌曲总数："+str)

wd=['30','31','30','29','30']
tq=['晴','雨','阴','霾','雪']
print(wd)
print(tq)
TQ={'wd':[30,31,30,29,30],
    'tq':['晴','雨','阴','霾','雪'],
    'day':['星期一','星期二','星期三','星期四','星期五','星期六','星期天']}
day=TQ['day']
print('today is :'+day[5])
print(max(TQ['wd']))

















