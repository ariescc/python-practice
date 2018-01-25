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
import stations
import requests
from prettytable import PrettyTable
from colorama import Fore

def cli():
    """Command-Line Interface"""
    arguments = docopt(__doc__, version='Tickets 1.0')
    date = arguments['<date>']
    from_station = stations.get_telecode(arguments['<from>']) # 从stations中获取，如果没有获取到返回None
    to_station = stations.get_telecode(arguments['<to>'])

    # 构建 url
    url = ('https://kyfw.12306.cn/otn/leftTicket/queryZ?'
           'leftTicketDTO.train_date={}&'
           'leftTicketDTO.from_station={}&'
           'leftTicketDTO.to_station={}&'
           'purpose_codes=ADULT').format(date, from_station, to_station)

    r = requests.get(url, verify = False)

    row_trains = r.json()['data']['result']
    pt = PrettyTable()
    pt._set_field_names('车次 车站 时间 历时 一等座 二等座 软卧 硬卧 硬座 无座'.split())
    for row_train in row_trains:
        data_list = row_train.split('|')
        train_no = data_list[3]
        from_station_code = data_list[6]
        to_station_code = data_list[7]
        from_station_name = ''
        to_station_name = ''
        start_time = data_list[8]
        arrive_time = data_list[9]
        time_duration = data_list[10]
        first_class_seat = data_list[31] or '--'
        second_class_seat = data_list[30] or '--'
        soft_sleep = data_list[23] or '--'
        hard_sleep = data_list[28] or '--'
        hard_seat = data_list[29] or '--'
        no_seat = data_list[33] or '--'
        pt.add_row([
            train_no,
            '\n'.join([stations.get_name(from_station_code), stations.get_name(to_station_code)]),
            '\n'.join([start_time, arrive_time]),
            time_duration,
            first_class_seat,
            second_class_seat,
            soft_sleep,
            hard_sleep,
            hard_seat,
            no_seat
        ])
        
    print(pt)



if __name__ == '__main__':
    cli()
