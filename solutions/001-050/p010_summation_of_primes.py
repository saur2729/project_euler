"""
Project Euler Problem 10 : Summation of Primes

The sum of the primes below 10 is 2 +3 +5 +7 =17.

Find the sum of all the primes below two million.

"""

from utils.math_helper import get_prime_sieve


def solve():
    n = 2_000_000
    all_primes = get_prime_sieve(n)

    return sum(all_primes)


if __name__ == "__main__":
    print(solve())  # returns --> 142913828922
