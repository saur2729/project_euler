"""
Project Euler Problem 26 : reciprocal cycles


A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

                        1/2	=0.5
                        1/3	=0.⁢(3)
                        1/4	=0.25
                        1/5	=0.2
                        1/6	=0.1⁢(6)
                        1/7	=0.⁢(142857)
                        1/8	=0.125
                        1/9	=0.⁢(1)
                        1/10	=0.1

Where 0.1⁢(6) means 0.166666⋯, and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of 𝑑 <1000 for which 1/𝑑 contains the longest recurring cycle in its decimal fraction part.

"""

# from utils.math_helper import *


def get_cycle_ln(d):
    rem = {}
    value = 1  # 1/d, as we start with 1
    pos = 0

    while value != 0:
        if value in rem:
            return pos - rem[value]

        rem[value] = pos
        # multiply by 10 and find remainder after dividing by val
        value = (value * 10) % d
        pos += 1

    return 0


def solve():
    d_max = 1000
    max_cycle = 1
    max_d = -1
    for i in range(1, d_max):
        tmp_cycle = get_cycle_ln(i)
        if tmp_cycle > max_cycle:
            max_cycle = tmp_cycle
            max_d = i

    return max_d


if __name__ == "__main__":
    print(solve())  # returns --> 983
