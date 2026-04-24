"""
Project Euler Problem 27 : quadratic primes

Euler discovered the remarkable quadratic formula:

                n^2 + n +41

It turns out that the formula will produce 40 primes for the consecutive integer values 0 ≤𝑛 ≤39. However, when 𝑛 =40,402 +40 +41 =40⁢(40 +1) +41 is divisible by 41, and certainly when n =41,412 +41 +41 is clearly divisible by 41.

The incredible formula n^2 - 79*n + 1601 was discovered, which produces 80 primes for the consecutive values 0 ≤𝑛 ≤79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

                n^2 + a^n + b, where |a| <1000 and |b| ≤1000

                where |n| is the modulus/absolute value of n
                e.g. |11| =11 and |-4| =4

Find the product of the coefficients, 𝑎 and 𝑏, for the quadratic expression that produces the maximum number of primes for consecutive values of 𝑛, starting with n =0.

"""

from utils.math_helper import get_prime_sieve


def solve():
    """
    n^2 + an + b ==> the o/p should be prime, if we keep n as 0, b should be prime and positive
    except for 2, all are odd prime,  so if we keep n==1, 1+a+b ==> to get odd prime, Odd(1)+Odd(b)+a = Odd ==> a should be odd
    so we need to loop through b from 2<>1000, a from -999<>999 (odds only) and check for prime
    """
    all_primes = set(get_prime_sieve(1_000_000))
    a_odd = [i for i in range(-999, 1000, 2)]

    ab_product = -1 * pow(10, 6)
    max_prime_seq = 0
    for b in [i for i in all_primes if i < 1000]:
        for a in a_odd:
            res_is_prime = True
            n = 0
            tmp_count = 0
            while res_is_prime:
                eq_res = n**2 + a * n + b
                if eq_res in all_primes:
                    tmp_count += 1
                    n += 1
                else:
                    res_is_prime = False
                    if tmp_count > max_prime_seq:
                        max_prime_seq = tmp_count
                        ab_product = a * b

    return ab_product


if __name__ == "__main__":
    print(solve())  # returns --> -59231 (negative)
