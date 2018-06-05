# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 09:00:49 2018

@author: lenovo
"""
"""py文件生成.exe文件
1..py文件路径    
2.英文
"""
#3.Anaconda cmd(安装生成exe插件)
#pip installer pyinstaller  
#4.打包程序,
#pyinstaller -F day02.py 

import urllib.request as r
import json
from xpinyin import Pinyin
from prettytable import PrettyTable

print("******************")
print("欢迎使用中国天气APP")
print("******************")
print("1.查看当前城市天气,2.未来五天城市天气(正午)，3.查看其它城市天气,4.保存当前城市")
menno=input("请输入菜单：")
p=Pinyin()

if menno == '1':
    print("1.查看当前城市天气")
    city=input("请输入城市名称:")
    city_pinyin = p.get_pinyin(city,'')
    address='http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'
    info=r.urlopen(address.format(city_pinyin)).read().decode('utf-8','ignore')
    #json(str)转换成dict
    data=json.loads(info)
    print("当日温度："+str(data["main"]["temp"]))
    print('当日最高温度：'+str(data['main']['temp_max']))
    print('实时气压：'+str(data['main']['pressure']))
    print('天气情况：'+str(data['weather'][0]['description']))
    print('-------------------------------------------')

if menno == '2':
    print("2.未来五天城市天气")
    import urllib.request as r
    city=input("请输入城市名称：")
    city_pinyin = p.get_pinyin(city,'')
    address='http://api.openweathermap.org/data/2.5/forecast?q={}&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
    info1=r.urlopen(address.format(city_pinyin)).read().decode('utf-8','ignore')
    table = PrettyTable(["时间", "  温度  ", "天气",'气压'])
    for i in range(37):
        w = json.loads(info1)
        time = w['list'][i]['dt_txt']
        temp = w['list'][i]['main']['temp']
        weather =  w['list'][i]['weather'][0]['description']
        pressure = w['list'][i]['main']['pressure']
        table.add_row([time,temp,weather,pressure])
        if i==4 or i==12 or i==20 or i==28:
            table.add_row(['------------------','------','------','------'])
    print(table)

if menno == '3':
    print("3.查看其它城市天气")
    
    
if menno == '4':
    print("4.保存当前城市")





