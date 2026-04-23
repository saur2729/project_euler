"""
Project Euler Problem 6: sum square difference

The sum of the squares of the first ten natural numbers is,
        1^2+2^2+...+10^2=385.
The square of the sum of the first ten natural numbers is,
        (1+2+...+10)2=552=3025.

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

"""

from utils.math_helper import *


def solve():
    # sum of n numbers is - s1 - (n*(n+1))/2
    # sum of squares of n numbers is  - s2 = n(n+1)(2n+1) / 6

    n = 100

    s1 = ((n * (n + 1)) / 2) ** 2
    s2 = (n * (n + 1) * (2 * n + 1)) / 6

    return s1 - s2


if __name__ == "__main__":
    print(solve())  # returns --> 25164150.0
