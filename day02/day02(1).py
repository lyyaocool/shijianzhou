# -*- coding: utf-8 -*-
"""
Created on Sun Jun  3 09:00:49 2018

@author: lenovo
"""

print("欢迎使用中国天气APP")
print("1.查看当前城市天气,2.未来五天城市天气(正午)，3.查看其它城市天气,4.保存当前城市")
menno=input("请输入菜单：")

if menno == '1':
    print("1.查看当前城市天气")
    import urllib.request as r
    city_pinyin=input("请输入城市拼音：")
    address='http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996'
    info=r.urlopen(address.format(city_pinyin)).read().decode('utf-8','ignore')
    #json(str)转换成dict
    import json
    data=json.loads(info)
    print('当日最高温度：'+str(data['main']['temp_max']))
    print('实时气压：'+str(data['main']['pressure']))
    print('天气情况：'+str(data['weather'][0]['description']))

if menno == '2':
    print("2.未来五天城市天气（正午）")
    import urllib.request as r
    city_pinyin=input("请输入城市拼音：")
    address='http://api.openweathermap.org/data/2.5/forecast?q={}&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric'
    info1=r.urlopen(address.format(city_pinyin)).read().decode('utf-8','ignore')
    import json
    data1=json.loads(info1)
    print("日期和时刻："+str(data1['list'][2]['dt_txt'])+";6月3日天气情况:"+str(data1["list"][2]['weather'][0]['description'])+";最高温度(摄氏度):"+str(data1["list"][2]["main"]["temp_max"])+";最低温度为(摄氏度):"+str(data1["list"][2]["main"]["temp_min"])+";实时气压："+str(data1["list"][2]['main']['pressure']))
    print("日期和时刻："+str(data1['list'][10]['dt_txt'])+";6月4日天气情况:"+str(data1["list"][10]['weather'][0]['description'])+";最高温度(摄氏度):"+str(data1["list"][10]["main"]["temp_max"])+";最低温度为(摄氏度):"+str(data1["list"][10]["main"]["temp_min"])+";实时气压："+str(data1["list"][10]['main']['pressure']))
    print("日期和时刻："+str(data1['list'][18]['dt_txt'])+";6月5日天气情况:"+str(data1["list"][18]['weather'][0]['description'])+";最高温度(摄氏度):"+str(data1["list"][18]["main"]["temp_max"])+";最低温度为(摄氏度):"+str(data1["list"][18]["main"]["temp_min"])+";实时气压："+str(data1["list"][18]['main']['pressure']))
    print("日期和时刻："+str(data1['list'][26]['dt_txt'])+";6月6日天气情况:"+str(data1["list"][26]['weather'][0]['description'])+";最高温度(摄氏度):"+str(data1["list"][26]["main"]["temp_max"])+";最低温度为(摄氏度):"+str(data1["list"][26]["main"]["temp_min"])+";实时气压："+str(data1["list"][26]['main']['pressure']))
    print("日期和时刻："+str(data1['list'][34]['dt_txt'])+";6月7日天气情况:"+str(data1["list"][34]['weather'][0]['description'])+";最高温度(摄氏度):"+str(data1["list"][34]["main"]["temp_max"])+";最低温度为(摄氏度):"+str(data1["list"][34]["main"]["temp_min"])+";实时气压："+str(data1["list"][34]['main']['pressure']))

if menno == '3':
    print("3.查看其它城市天气")
    
    
if menno == '3':
    print("4.保存当前城市")




