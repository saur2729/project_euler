"""
Project Euler Problem 21 : amicable numbers

Let 𝑑⁡(𝑛) be defined as the sum of proper divisors of 𝑛 (numbers less than 𝑛 which divide evenly into 𝑛).
If 𝑑⁡(𝑎) =𝑏 and 𝑑⁡(𝑏) =𝑎, where 𝑎 ≠𝑏, then 𝑎 and 𝑏 are an amicable pair and each of 𝑎 and 𝑏 are called amicable numbers.

For example, the proper divisors of 220 are 1,2,4,5,10,11,20,22,44,55 and 110; therefore 𝑑⁡(220) =284. The proper divisors of 284 are 1,2,4,71 and 142; so 𝑑⁡(284) =220.

Evaluate the sum of all the amicable numbers under 10000.

"""

from utils.math_helper import find_factors_simple

divisor_sum_map = {1: 1}


def is_amicable(i):
    if i in divisor_sum_map:
        a = divisor_sum_map[i]
    else:
        a = sum(find_factors_simple(i)[:-1])
        divisor_sum_map[i] = a

    if a in divisor_sum_map:
        b = divisor_sum_map[a]
    else:
        b = sum(find_factors_simple(a)[:-1])
        divisor_sum_map[a] = b

    return a, b, (i == b and a != b)


def solve():
    n = 10000
    amicable_nos = set()

    for i in range(1, n):
        a, b, amicable_status = is_amicable(i)
        if amicable_status:
            amicable_nos.update([a, b])

    return sum(amicable_nos)


if __name__ == "__main__":
    print(solve())  # returns --> 31626
