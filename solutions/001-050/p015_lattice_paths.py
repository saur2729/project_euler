"""
Project Euler Problem 15 : lattice paths

"""

import math


def solve():
    n = 20
    # for 20x20 grid, we will have 40 moves and need to select 20
    return math.comb(40, 20)


if __name__ == "__main__":
    print(solve())  # returns --> 137846528820
