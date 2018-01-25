import sys
import csv
from urllib import request
from bs4 import BeautifulSoup

from house_info import house

# 将cities.csv数据存储到字典中
def get_city_dict():
    # 创建字典
    city_dict = {}
    # 将cities.csv中数据转换成字典形式
    with open('cities.csv', 'r') as f:
        city_list = csv.reader(f)
        for city in city_list:
            city_dict[city[0]] = city[1]
    return city_dict

# 将城市对应的区域信息保存到字典中
def get_district_dict(url):
    district_dict = {}

    html = request.urlopen(url).read()
    bsobj = BeautifulSoup(html, 'lxml')

    district_tags = bsobj.find('div', {'data-role': 'ershoufang'}).findChildren('a')

    """
    区域信息在 <div data-role="ershoufang">下的每一个<a>标签中

    内容如下：
        <a href="/ershoufang/dongcheng/" title="北京东城在售二手房 ">东城</a>
    """
    
    for district in district_tags:
        # 对应区域的 url
        district_url = district.get('href')
        # 对应区域的 name
        district_name = district.get_text()

        # {name: url} 保存到字典中
        district_dict[district_name] = district_url

    return district_dict

# 入口函数
def run():
    # 获取cities.csv字典
    city_dict = get_city_dict()

    input_city = input('请输入城市名：')
    # 获取城市 url（cities.csv中）
    city_url = city_dict.get(input_city)

    if not city_url:
        print('输入错误！')
        sys.exit()

    ershoufang_city_url = city_url + 'ershoufang/'
    print(ershoufang_city_url)

    # 构造该城市的区域字典
    district_dict = get_district_dict(ershoufang_city_url)

    input_district = input('请输入地区：')
    district_url = district_dict.get(input_district)

    if not district_url:
        print('输入错误！')
        sys.exit()

    house_info_url = city_url + district_url[1:] 
    print(house_info_url)
    house(house_info_url)
    

if __name__ == '__main__':
    run()

