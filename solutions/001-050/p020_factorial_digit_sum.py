"""
Project Euler Problem 20 : factorial digit sum

𝑛! means 𝑛 ×(𝑛 −1) ×⋯ ×3 ×2 ×1.

For example, 10! =10 ×9 ×⋯ ×3 ×2 ×1 =3628800,
and the sum of the digits in the number 10! is 3 +6 +2 +8 +8 +0 +0 =27.

Find the sum of the digits in the number 100!.

"""

# from utils.math_helper import *


def get_factorial(n):
    if n == 1:
        return 1
    return n * get_factorial(n - 1)


def solve():
    n = 100
    n_fact = get_factorial(n)
    digit_sum = 0
    while n_fact > 0:
        digit_sum += n_fact % 10
        n_fact = n_fact // 10

    return digit_sum


if __name__ == "__main__":
    print(solve())  # returns --> 648
