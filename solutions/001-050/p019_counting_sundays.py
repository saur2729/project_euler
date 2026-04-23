"""
Project Euler Problem 19 : counting sundays

You are given the following information, but you may prefer to do some research for yourself.

    - 1 Jan 1900 was a Monday.
    - Thirty days has September, April, June and November.
      All the rest have thirty-one,
      Saving February alone,
      Which has twenty-eight, rain or shine.
      And on leap years, twenty-nine.
    - A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

"""

import datetime as dt


def solve():
    count = 0
    # Loop through every year and every month
    for year in range(1901, 2001):
        for month in range(1, 13):
            # weekday() returns 0 for Monday, 6 for Sunday
            if dt.date(year, month, 1).weekday() == 6:
                count += 1
    return count


if __name__ == "__main__":
    print(solve())  # returns --> 171
