#!/usr/bin/env python3

import argparse
import datetime

def add_time_duration(start_time, duration):
    FMT = '%I:%M%p'
    start_time = datetime.datetime.strptime(start_time, FMT)
    
    hours, minutes, seconds = map(int, duration.split(':'))
    end_time = start_time + datetime.timedelta(hours=hours, minutes=minutes, seconds=seconds)

    return end_time.strftime(FMT)

def main():
    parser = argparse.ArgumentParser(description='Add duration to time.')
    parser.add_argument('start_time', type=str, help='The start time in 12-hour format (e.g., 07:30PM).')
    parser.add_argument('duration', type=str, help='The duration to be added in the format (HH:MM:SS).')

    args = parser.parse_args()
    
    print(add_time_duration(args.start_time.upper(), args.duration))

if __name__ == '__main__':
    main()

