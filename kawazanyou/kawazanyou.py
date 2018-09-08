#!/usr/bin/env python
import argparse

parser = argparse.ArgumentParser(description='kawazanyou')

parser.add_argument('-i', '--initial',
                    required=True,
                    type=int,
                    help='Initial value')
parser.add_argument('-r', '--rate',
                    required=True,
                    type=int,
                    help='Annual interest rate')
parser.add_argument('-s', '--saving',
                    required=True,
                    type=int,
                    help="Annual saving")
parser.add_argument('-t', '--term',
                    required=True,
                    type=int, help="term")
parser.add_argument('-d', '--debug',
                    required=False,
                    action='store_true',
                    help="debug mode")


args = parser.parse_args()

initial = args.initial
rate = args.rate
saving = args.saving
term = args.term
debug = args.debug


if debug:
    print('initial : {}'.format(initial))
    print('rate    : {} %'.format(rate))
    print('saving  : {}'.format(saving))
    print('term    : {} year'.format(term))

actual = initial

print('year, actual, profit')

for var in range(0, term):
    total_saving_amount = saving * 12
    actual += total_saving_amount
    profit = actual * (rate / 100)
    actual += profit
    print('{},{},{}'.format(var, actual, profit))
