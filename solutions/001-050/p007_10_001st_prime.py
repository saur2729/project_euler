"""
Project Euler Problem 7 : 10 001st Prime

By listing the first six prime numbers: 2,3,5,7,11, and 13, we can see that the 6th prime is 13.
What is the 10,001 st prime number?
"""

from utils.math_helper import get_prime_sieve


def solve():
    prime_l = get_prime_sieve(200000)

    return prime_l[10000]


if __name__ == "__main__":
    print(solve())  # returns --> 104743
