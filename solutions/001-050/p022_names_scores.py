import os

"""
Project Euler Problem 22 : names scores

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 +15 +12 +9 +14 =53, is the 938th name in the list. So, COLIN would obtain a score of 938 ×53 =49714.

What is the total of all the name scores in the file?

"""

# from utils.math_helper import *
import requests


def solve():
    url = "https://projecteuler.net/resources/documents/0022_names.txt"
    raw_data = requests.get(url).text

    data = raw_data.replace(",,", ",").replace('"', "").split(",")
    data = sorted(data)

    total = 0
    for index, name in enumerate(data, start=1):
        value = sum(ord(ch) - 64 for ch in name)
        total += value * index

    return total


if __name__ == "__main__":
    print(solve())  # returns --> 871198282
