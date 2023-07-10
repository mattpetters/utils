#!/usr/bin/env python3
import datetime
import argparse
from termcolor import colored
from art import *

def hourglass(n, n2=1, filler_char=' ', lived_percentage=0):
    line_to_start = n*2 - int(lived_percentage / 100 * (n*2))
    hourglass_string = ""

    if n == n2:
        hourglass_string += '{:{filler}^{width}}'.format(filler_char.join('{}'.format(n)), width=n*2-1, filler=filler_char) + "\n"
        if n2 > line_to_start:
            return hourglass_string, True
        else:
            return hourglass_string, False

    hourglass_string += '{:{filler}^{width}}'.format(filler_char.join(str(i) for i in range(n2, n+1)), width=n*2-1, filler=filler_char) + "\n"
    sub_hourglass_string, color_changed = hourglass(n, n2+1, filler_char, lived_percentage)
    hourglass_string += sub_hourglass_string
    hourglass_string += '{:{filler}^{width}}'.format(filler_char.join(str(i) for i in range(n2, n+1)), width=n*2-1, filler=filler_char) + "\n"
    if n2 > line_to_start:
        color_changed = True

    return hourglass_string, color_changed


def calculate_remaining_time(birthday, life_expectancy_years):
    now = datetime.datetime.now()
    life_expectancy = datetime.timedelta(days=life_expectancy_years*365.25) # Considering leap years
    birth_date = datetime.datetime.strptime(birthday, "%d-%m-%Y")
    lived = now - birth_date
    remaining = life_expectancy - lived
    lived_percentage = (lived.total_seconds() / life_expectancy.total_seconds()) * 100
    remaining_percentage = 100 - lived_percentage

    return lived, remaining, lived_percentage, remaining_percentage

def convert_seconds_to_hms(seconds):
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return hours, minutes, seconds

def main():
    parser = argparse.ArgumentParser(description="Calculate the time lived and remaining based on average life expectancy.")
    parser.add_argument('-b', '--birthday', required=True, help="Your birthday (format: dd-mm-yyyy)")
    parser.add_argument('-d', '--death_age', type=float, default=73.3, help="Expected age at death (default: 73.3)")
    args = parser.parse_args()

    lived, remaining, lived_percentage, remaining_percentage = calculate_remaining_time(args.birthday, args.death_age)

    print(colored("\nHourglass of Life \n", 'white'))
    hourglass_string, color_changed = hourglass(7, lived_percentage=lived_percentage)
    green_part, _, white_part = hourglass_string.rpartition("\n")
    if color_changed:
        print(colored(green_part, 'green'))
        print(colored(white_part, 'white'))
    else:
        print(colored(hourglass_string, 'white'))


    lived_hours, lived_minutes, lived_seconds = convert_seconds_to_hms(lived.seconds)
    print(colored("\nLived time: {} days, {} hours, {} minutes, {} seconds".format(lived.days, lived_hours, lived_minutes, lived_seconds), 'green'))
    remaining_hours, remaining_minutes, remaining_seconds = convert_seconds_to_hms(remaining.seconds)
    print(colored("\nRemaining time: {} days, {} hours, {} minutes, {} seconds".format(remaining.days, remaining_hours, remaining_minutes, remaining_seconds), 'red'))
    print(colored("\nLived life: ", 'green'))
    print(colored(text2art("{:.2f}%".format(lived_percentage)), 'green'))

    # print(colored("\nHourglass of Life (Remaining Part)\n", 'cyan'))
    # hourglass(7, filler_char=' ', color='white')
    
    print(colored("\nRemaining life: ", 'red'))
    print(colored(text2art("{:.2f}%".format(remaining_percentage)), 'red'))

if __name__ == "__main__":
    main()

