#!/usr/bin/env python
import argparse

parser = argparse.ArgumentParser(description='kawazanyou')

parser.add_argument('-i', '--initial', type=int, help='Initial value')
parser.add_argument('-r', '--rate', type=int, help='Annual interest rate')
parser.add_argument('-s', '--saving', type=int, help="Annual saving")
parser.add_argument('-t', '--term', type=int, help="term")


args = parser.parse_args()

initial = args.initial
rate = args.rate
saving = args.saving
term = args.term

print('initial : {}'.format(initial))
print('rate    : {} %'.format(rate))
print('saving  : {}'.format(saving))
print('term    : {} year'.format(term))

actual = initial

for var in range(0, term):
    total_saving_amount = saving * 12
    actual += total_saving_amount
    profit = actual * (rate / 100)
    actual += profit
    print('{} : {} ({})'.format(var, actual, profit))
