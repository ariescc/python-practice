#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 使用方法 python markdown_convert.py filename

import sys
import markdown
import codecs


css = '''
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<style type="text/css">
<!-- 此处省略掉markdown的css样式，因为太长了 -->
</style>
'''

def main():
    in_file = 'score.md'
    out_file = 'score.html'

    input_file = codecs.open(in_file, mode="r", encoding="utf-8")
    text = input_file.read()
    html = markdown.markdown(text)

    output_file = codecs.open(out_file, "w",encoding="utf-8",errors="xmlcharrefreplace")
    output_file.write(css+html)

if __name__ == "__main__":
   main()