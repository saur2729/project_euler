"""
Project Euler Problem 4: largest palindrome product

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
Find the largest palindrome made from the product of two 3-digit numbers.


"""

# from utils.math_helper import *


def is_palindrome(sample) -> bool:
    if not isinstance(sample, str):
        sample = str(sample)

    return sample == sample[::-1]


def solve():
    # the min and max product of two three digit numbers are
    # 10000 = 100 x 100
    # 998001 = 999 * 999
    # for palindorme of 6 digits, I see its divisible by 11
    # can use 2 pointers i and j, and one should be multiple of 11

    max_palindrome = 0
    start_range = (1000 // 11) * 11
    for i in range(start_range, 99, -11):
        for j in range(999, 99, -1):
            product = i * j

            if product < max_palindrome:
                break

            if is_palindrome(product):
                max_palindrome = product

    return max_palindrome


if __name__ == "__main__":
    ans = solve()
    print(ans)  # returns --> 906609
