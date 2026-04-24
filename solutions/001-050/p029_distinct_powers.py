"""
Project Euler Problem 29 : distinct powers

"""

# from utils.math_helper import *


def solve():
    # TODO : for higher counts, it can also be done by finding
    # all duplicates power values and removing it from the total list
    return len(set(a**b for a in range(2, 101) for b in range(2, 101)))


if __name__ == "__main__":
    print(solve())  # returns --> 9183
