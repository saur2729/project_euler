"""
Project Euler Problem 17 : number letter counts

    If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 +3 +5 +4 +4 =19 letters used in total.

    If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?


    NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.
"""

# from utils.math_helper import *


def num_to_word(n):
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = [
        "ten",
        "eleven",
        "twelve",
        "thirteen",
        "fourteen",
        "fifteen",
        "sixteen",
        "seventeen",
        "eighteen",
        "nineteen",
    ]
    tens = [
        "",
        "",
        "twenty",
        "thirty",
        "forty",
        "fifty",
        "sixty",
        "seventy",
        "eighty",
        "ninety",
    ]

    if n == 1000:
        return "onethousand"

    res = ""

    # Check for hundreds
    if n >= 100:
        res += ones[n // 100] + "hundred"
        if n % 100 != 0:
            res += "and"

    # check for tens and ones
    n = n % 100
    if 10 <= n <= 19:
        res += teens[n % 10]
    else:
        # split tens and ones
        at_tens, at_ones = n // 10, n % 10
        res += tens[at_tens]
        res += ones[at_ones]

    return res


def solve():
    n = 1000

    return sum([len(num_to_word(i)) for i in range(1, 1001)])


if __name__ == "__main__":
    print(solve())  # returns --> 21124
