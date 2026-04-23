"""
Project Euler Problem 9 : Special Pythagorean Triplet

    A Pythagorean triplet is a set of three natural numbers, 𝑎 < 𝑏 < 𝑐, for which,
            𝑎^2 + 𝑏^2 = 𝑐2.

    For example, 3^2 + 4^2 = 9 + 16 = 25 = 52.

    There exists exactly one Pythagorean triplet for which 𝑎 +𝑏 +𝑐 = 1000.
    Find the product 𝑎⁢𝑏⁢𝑐.

"""

from utils.math_helper import find_factors_simple
import math


def solve():
    n = 1000
    # using Euclid's formula, a b c can be defined as - i^2 - j^2 , 2ij, i^2 + j^2

    # since a+b+c = 1000 , we can put values,   i^2 - j^2 + 2ij + i^2 + j^2 ~= 2i^2 + 2ij
    # so 2i(i+j) = 1000 ==> i(i+j) = 500 or j = (500/i - i)

    # Solvijg i(i+j) = 500
    factors_500 = find_factors_simple(500)

    # since i should be factor of 500 and i > j
    tmp_i, tmp_j = 0, 0
    for i in factors_500[1:-1]:  # removing 1 and number itself from factors
        j = (500 / i) - i
        # if number is float OR i<j, continue
        if (j != int(j)) or (i < j) or (j < 0):
            continue
        tmp_i, tmp_j = i, j

    print(tmp_i, tmp_j)
    a, b, c = tmp_i**2 - tmp_j**2, 2 * tmp_i * tmp_j, tmp_i**2 + tmp_j**2

    return int(a * b * c)


if __name__ == "__main__":
    print(solve())  # returns --> 31875000
