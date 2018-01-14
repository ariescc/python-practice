#!/usr/bin/python
# encoding: utf-8 
import jieba
from wordcloud import WordCloud
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

text = '李小璐给王思聪买了微博热搜'

# 强调特殊名词
jieba.suggest_freq(('微博'), True)
jieba.suggest_freq(('热搜'), True)

#jieba.load_userdict('dict.txt')

result = jieba.cut(text)
cloud_text = ','.join(result)

print(cloud_text)

# 生成词云
wc = WordCloud(
    background_color = 'white',
    max_words = 200,
    font_path = 'arial.ttf',
    min_font_size = 15,
    max_font_size = 50,
    width = 400 # 图幅宽度
)

wc.generate(cloud_text)
wc.to_file('pic.png')

