import re
from collections import defaultdict

import datetime
from operator import itemgetter


def main():
    part_one()


def part_one():
    data = []
    with open('input.txt', 'r') as input_file:
        for line in input_file:
            data.append({'date': line[1:17], 'action': line[19:]})

    data = sorted(data, key=date_key)

    print data

    sleep_dic = defaultdict(int)
    current_guard = -1
    falls_sleep_date = datetime.datetime.now()
    for line in data:
        if 'Guard' in line['action']:
            current_guard = [int(n) for n in re.findall(r'\d+', line['action'])][0]
        if 'falls asleep' in line['action']:
            date_list = [int(n) for n in re.findall(r'\d+', line['date'])]
            falls_sleep_date = datetime.datetime(year=date_list[0], month=date_list[1], day=date_list[2],
                                                 hour=date_list[3], minute=date_list[4])
        if 'wakes up' in line['action']:
            date_list = [int(n) for n in re.findall(r'\d+', line['date'])]
            wakes_up_date = datetime.datetime(year=date_list[0], month=date_list[1], day=date_list[2],
                                              hour=date_list[3], minute=date_list[4])
            sleep_dic[current_guard] += (wakes_up_date - falls_sleep_date).total_seconds() / 60.0

    sleep_dic = sorted(sleep_dic.items(), key=itemgetter(1))

    guard = sleep_dic[-1]

    print guard[0] * guard[1]


def date_key(item):
    return datetime.datetime.strptime(item['date'], '%Y-%m-%d %H:%M')


if __name__ == '__main__':
    main()
