"""
Project Euler Problem 25 :  1000-digit Fibonacci Number

The Fibonacci sequence is defined by the recurrence relation:
                𝐹𝑛 =𝐹𝑛−1 +𝐹𝑛−2, where 𝐹1 =1 and 𝐹2 =1.

Hence the first 12 terms will be:

                𝐹1	=1
                𝐹2	=1
                𝐹3	=2
                𝐹4	=3
                𝐹5	=5
                𝐹6	=8
                𝐹7	=13
                𝐹8	=21
                𝐹9	=34
                𝐹10	=55
                𝐹11	=89
                𝐹12	=144

The 12th term, 𝐹12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

"""

# from utils.math_helper import *


def solve():
    a, b = 1, 1
    index = 2

    n_digits = 1000 - 1

    while True:
        index += 1
        tmp = a + b
        a = b
        b = tmp

        if b // pow(10, n_digits) > 0:
            return index


if __name__ == "__main__":
    print(solve())  # returns --> 4782
