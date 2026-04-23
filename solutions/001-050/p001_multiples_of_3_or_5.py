"""
Project Euler Problem 1: multiples of 3 or 5

Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.Find the sum of all the multiples of 3 or 5 below 1000.
"""

# from utils.math_helper import *


def solve():
    # lazy approach
    # return sum(set(range(0, 1000, 3)) | set(range(0, 1000, 5)))

    # optimized approach
    """
    sum of N numbers is (n*(n+1)) / 2
    below 1000, the 3 series would be 3,6,9.., so the formula will be (d * n * (n+1)) / 2)
    n we can calculate all numbers divided by 3 below 1000 and same for others
    """
    d_3 = int(999 / 3)
    d_5 = int(999 / 5)
    d_15 = int(999 / 15)

    final_sum = (
        ((3 * d_3 * (d_3 + 1)) // 2)  # for 3 series
        + ((5 * d_5 * (d_5 + 1)) // 2)  # for 5 series
        - (
            (15 * d_15 * (d_15 + 1)) // 2
        )  # subtract 15 series as its common between 3 x 5
    )

    return final_sum


if __name__ == "__main__":
    ans = solve()
    print(ans)  # prints --> 233168
