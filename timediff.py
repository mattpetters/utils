#!/usr/bin/env python3

import argparse
import datetime

def calculate_time_difference(start_time, end_time):
    FMT = '%I:%M%p'
    tdelta = datetime.datetime.strptime(end_time, FMT) - datetime.datetime.strptime(start_time, FMT)

    if tdelta.days < 0:
        tdelta = datetime.timedelta(days=0,
                seconds=tdelta.seconds, microseconds=tdelta.microseconds)
    return tdelta

def main():
    parser = argparse.ArgumentParser(description='Calculate time difference.')
    parser.add_argument('start_time', type=str, help='The start time in 12-hour format (e.g., 07:30PM).')
    parser.add_argument('end_time', type=str, help='The end time in 12-hour format (e.g., 08:30AM).')

    args = parser.parse_args()
    
    print(calculate_time_difference(args.start_time.upper(), args.end_time.upper()))

if __name__ == '__main__':
    main()

