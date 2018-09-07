#!/usr/bin/env python
import argparse

parser = argparse.ArgumentParser(description='kawazanyou')

parser.add_argument('-i','--initial', type=int, help='Initial value')
parser.add_argument('-r','--rate', type=int, help='Annual interest rate')
parser.add_argument('-s', '--saving', type=int, help="Annual saving")


args = parser.parse_args()
if(args.display):
  print(args.accumulate(args.initial))