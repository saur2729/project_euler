"""
Project Euler Problem 28 : number spiral diagonals

Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

                    21 22 23 24 25
                    20  7  8  9 10
                    19  6  1  2 11
                    18  5  4  3 12
                    17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

"""

# from utils.math_helper import *


def solve():
    # 1 + (1+2*1) + (1+2*2) + (1+2*3) + (1+2*4) + (1+2*6) + (1+2*8) + (1+2*8) + (1+2*8) + (1+2*8) + (1+2*8) + (1+2*8) + (1+2*8) + (1+2*8)
    # 1       3         5         7        9          13       17         21        25       31        37         43       49         57

    n = 1
    diag_sum = 1
    size = 2 * n + 1
    diag_ele = 1

    while size <= 1001:
        for _ in range(4):
            diag_ele += 2 * n
            diag_sum += diag_ele
        n += 1
        size = 2 * n + 1

    return diag_sum


if __name__ == "__main__":
    print(solve())  # returns --> 669171001
