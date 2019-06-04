#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse

parser = argparse.ArgumentParser(description='culc_scrum_point')

parser.add_argument('-p', '--point',
                    required=True,
                    type=float,
                    help='total point')
parser.add_argument('-d', '--day',
                    required=True,
                    type=int,
                    help='day number')
parser.add_argument('-t', '--term',
                    required=True,
                    type=int,
                    help='term number')
parser.add_argument('-c', '--complete',
                    required=True,
                    type=float,
                    help='complete point')


args = parser.parse_args()

point_number = float(args.point)
day = float(args.day)
complete_point = float(args.complete)
term = float(args.term)

point_by_day = round(point_number / term, 2)
scheduled_point = point_by_day * day

if not term == day:
    point_to_complete_by_day = round(
        (point_number - complete_point) / (term - day), 2)
else:
    point_to_complete_by_day = 0

print(f'総ポイント数　　　　　：{point_number}')
print(f'実消化ポイント数　　　：{complete_point}')
print(f'予定消化ポイント数　　：{scheduled_point}')
print(f'遅れ　　　　　　　　　：{scheduled_point - complete_point}')
print(f'１日あたりのポイント数：{point_to_complete_by_day}')
