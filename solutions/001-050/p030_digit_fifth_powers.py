"""
Project Euler Problem 30 : digit fifth powers

"""

# from utils.math_helper import *


def get_digit_sum(n):
    power_map = [i**5 for i in range(10)]
    tmp_sum = 0

    while n > 0:
        digit = n % 10
        n //= 10
        tmp_sum += power_map[digit]

    return tmp_sum


def solve():

    upper_limit = 6 * (9**5) + 1  # considering all digits are 9 and max 6 digits

    final_sum = 0

    for i in range(2, upper_limit):
        if i == get_digit_sum(i):
            final_sum += i

    return final_sum


if __name__ == "__main__":
    print(solve())  # returns --> 443839
