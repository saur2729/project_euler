"""
Project Euler Problem 23 : non abundant sums

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 +2 +4 +7 +14 =28, which means that 28 is a perfect number.

A number 𝑛 is called deficient if the sum of its proper divisors is less than 𝑛 and it is called abundant if this sum exceeds 𝑛.

As 12 is the smallest abundant number, 1 +2 +3 +4 +6 =16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

"""

from utils.math_helper import find_factors_simple

_LIMIT = 28123


def all_abundant():
    abundant_l = []
    for i in range(1, _LIMIT + 1):
        if sum(find_factors_simple(i)[:-1]) > i:
            abundant_l.append(i)

    return abundant_l


def abundant_sum(a_list):
    abundant_sum_l = set()
    for i in a_list:
        for j in a_list:
            abundant_sum_l.add(i + j)
    return list(abundant_sum_l)


def solve():
    a_list = all_abundant()

    # Use a boolean array to track which numbers can be written as a sum
    # This is much faster and memory-efficient than a set for this range
    is_abundant_sum = [False] * (_LIMIT + 1)

    for i in range(len(a_list)):
        for j in range(i, len(a_list)):
            s = a_list[i] + a_list[j]
            if s <= _LIMIT:
                is_abundant_sum[s] = True
            else:
                # Since abundants is sorted, we can break early
                break

    # Sum only the numbers that were never marked 'True'
    total = sum(i for i in range(1, _LIMIT + 1) if not is_abundant_sum[i])
    return total


if __name__ == "__main__":
    print(solve())  # returns -->
