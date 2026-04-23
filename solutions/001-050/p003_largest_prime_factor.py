"""
Problem 3: Largest Prime Factor

The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600,851,475,143?

"""

from utils.math_helper import get_prime_sieve


def solve():
    n = 600851475143

    # get primes using sieve
    # we can simply check for root of n primes only
    root_n = int(pow(n, 0.5)) + 1
    primes = get_prime_sieve(root_n)

    has_largest_prime = False
    largest_prime = -1

    for num in primes:
        if n % num == 0 and num != n:
            has_largest_prime = True
            largest_prime = num if num > largest_prime else largest_prime

        if num == n and (not has_largest_prime):
            return n

    return largest_prime if largest_prime != -1 else n


if __name__ == "__main__":
    ans = solve()
    print(ans)  # ans --> 6857
