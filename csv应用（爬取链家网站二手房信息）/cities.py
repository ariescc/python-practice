import csv
from urllib import request
from bs4 import BeautifulSoup

url = 'https://www.lianjia.com'

# 获取 html 页面
html = request.urlopen(url).read()

# 获取 BeautifulSoup 对象,用 html5lib 解析
bsobj = BeautifulSoup(html, 'lxml')

# 得到 class = "fc-main clear" 的 <div> 下所有 <a> 标签
city_tags = bsobj.find('div', {'class': 'fc-main clear'}).findChildren('a')

"""
 city_tags 内数据的格式如下:
 
    <a title="天津房产网" href="https://tj.lianjia.com/">天津</a>
"""

# 将每一条数据抽离，保存在 cities.csv 文件中
with open('cities.csv', 'w') as f:
    fw = csv.writer(f)
    for city_tag in city_tags:
        # 获取 <a> 标签的 href 链接
        city_url = city_tag.get('href')
        # 获取 <a> 标签的文字，如天津
        city_name = city_tag.get_text()
        fw.writerow((city_name, city_url))
        print(city_name, city_url)

