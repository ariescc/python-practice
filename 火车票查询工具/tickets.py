#!/usr/bin/env python
# encoding: utf-8

"""
命令行火车票查看器

Usage:
    tickets [-gdtkz] <from> <to> <date>

Options:
    -h, --help  显示帮助菜单
    -g          高铁
    -d          动车
    -t          特快
    -k          快速
    -z          直达

EXAMPLE:
    tickets -z 西安 北京西 2018-01-20

"""
from docopt import docopt
from stations import stations

def cli():
    """Command-Line Interface"""
    arguments = docopt(__doc__)

    from_station = stations.get(arguments['<from>'])

    to_station = stations.get(arguments['<to>'])

    date = arguments['<date>']

    # 构建 url
    url = 'https://kyfw.12306.cn/otn/lcxxcx/queryz?purpose_codes=ADULT&queryDate={}&from_station={}&to_station={}'.format(
        date, from_station, to_station
    )

    r = requests.get(url, verify = False)

    print(r.json())


if __name__ == '__main__':
    cli()
