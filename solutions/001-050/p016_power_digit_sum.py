"""
Project Euler Problem 16 : power digit sum

2^15 =32768 and the sum of its digits is 3 +2 +7 +6 +8 =26.

What is the sum of the digits of the number 2^1000?

"""

# from utils.math_helper import *


def get_digit_sum(n):
    if n == 0:
        return 0
    return n % 10 + get_digit_sum(n // 10)


def solve():
    num = pow(2, 1000)

    return get_digit_sum(num)


if __name__ == "__main__":
    print(solve())  # returns --> 1366
