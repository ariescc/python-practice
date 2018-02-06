"""
调用有道翻译api
"""
import requests
import numpy as np
import sys
import hashlib

# app_id
app_id = '20180206000121349'
# 随机数
salt = np.random.randint(-sys.maxsize, sys.maxsize)
# 密钥
app_key = 'LebJVuapyHl8zQNEimBT'

# Language
language = {
    'China': 'zh',
    'America': 'en'
}


# md5加密
def handleMd5(string):
    md5 = hashlib.md5(string.encode('utf-8')).hexdigest()
    return md5


# 中文  =>  英文
def translateZHtoEN():
    query = input('请输入中文：')
    url = url_builder(query, 'China', 'America')
    req_api(url)

# 英文  =>  中文
def translateENtoZH():
    query = input('请输入英文：')
    url = url_builder(query, 'America', 'China')
    req_api(url)


# 调用 api
def req_api(url):
    req = requests.get(url, verify=False)
    lst = req.json()['trans_result']
    res = lst[0]['dst']
    print('翻译结果： ')
    print(res)
    print('\n')


def url_builder(query, _from, _to):
    fo = language[_from]
    to = language[_to]
    string = app_id + query + str(salt) + app_key
    sign = handleMd5(string)
    url = ('http://api.fanyi.baidu.com/api/trans/vip/translate?'
           'q={}&'
           'from={}&'
           'to={}&'
           'appid={}&'
           'salt={}&'
           'sign={}').format(query, fo, to, app_id, salt, sign)
    #print(url)
    return url


if __name__ == '__main__':
    print('************** ariescc, you are good ***********')
    print('--- 中文 to 英文 ： 1')
    print('--- 英文 to 中文 ： 2')
    #print('--- 文件读取 （英文 to 中文）： 3')
    choice = int(input('请选择：'))
    if choice == 1:
        while True:
            translateZHtoEN()
    elif choice == 2:
        while True:
            translateENtoZH()
    #elif choice == 3:
    #    translateTXT()
    else:
        print('illegal choice!!')

