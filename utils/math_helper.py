import math

"""
Math related functions which can be easily used everywhere
"""


def get_prime_sieve(n):
    """Sieve of Eratosthenes optimized for memory and speed."""
    if n < 2:
        return []

    if n == 2:
        return [2]

    # Sieve only odd numbers, ignoring even as they are multiple of 2
    size = (n - 1) // 2
    sieve = [True] * (size + 1)

    for i in range(int(size**0.5) + 1):
        if sieve[i]:
            p = 2 * i + 3  # The actual prime number
            # Mark multiples starting from p*p
            start = (p * p - 3) // 2
            sieve[start::p] = [False] * ((size - start) // p + 1)

    return [2] + [
        2 * i + 3 for i, prime in enumerate(sieve) if prime and 2 * i + 3 <= n
    ]


def is_palindrome(val):
    """Checks if a number or string is a palindrome."""
    s = str(val)
    return s == s[::-1]
