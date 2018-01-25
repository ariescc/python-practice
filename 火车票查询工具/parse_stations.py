#!/usr/bin/env python
# encoding: utf-8

"""
找出所有的火车站
"""

import re
import requests
from pprint import pprint

url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.8971'

response = requests.get(url, verify = False) # verify = False添加参数禁止证书验证
stations = re.findall(u'([\u4e00-\u9fa5]+)\|([A-Z]+)', response.text)
print(dict(stations).keys())
print(dict(stations).values())
