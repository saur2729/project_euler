"""
Project Euler Problem 5: smallest multiple

    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

# from utils.math_helper import *
import math


def solve():
    n = 20
    ans = 1
    for i in range(1, n + 1):
        # LCM(a, b) = (a * b) // GCD(a, b)
        ans = (ans * i) // math.gcd(ans, i)  # using greatest common divisor
    return ans


if __name__ == "__main__":
    ans = solve()
    print(ans)  # prints --> 232792560
