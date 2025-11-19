# -*- coding: utf-8 -*-
"""
Created on Tue Nov 18 16:59:33 2025

@author: 两句话
"""

#用户输入星座，用空格分隔
user_input = input("请输入星座（用空格分隔，例如：处女座 金牛座 水瓶座）：")
constellation = user_input.split()
#创建星象列表
signs=["水象","风象","土象","火象"]
#创建不同星象的星座列表
water_signs=["天蝎座","巨蟹座","双鱼座"]
air_signs=["水瓶座","双子座","天秤座"]
earth_signs=["处女座","金牛座","摩羯座"]
fire_signs=["白羊座","射手座","狮子座"]


#循环遍历列表并判断列表中是否存在星象，若存在则将对应星座替换为其星象
for i,star_signs in enumerate(constellation):
    if star_signs in water_signs:
        constellation[i] = "水象"
    elif star_signs in air_signs:
        constellation[i] = "风象"
    elif star_signs in earth_signs:
        constellation[i] = "土象"
    elif star_signs in fire_signs:
        constellation[i] = "火象"

#将列表创建为集合去重
signs_set=set(constellation)
#输出星象
print("存在的星象有："+str(signs_set))

#定义计数函数对星象进行计算
def count_signs(sign_list, sign_type):
    num=sign_list.count(sign_type)
    """统计列表中某种星象的数量"""
    return num

#使用循环调用计数函数并输出
for sign_type in signs:
    count = count_signs(constellation, sign_type)
    print(sign_type + "：" + str(count))