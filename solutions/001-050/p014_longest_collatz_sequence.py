"""
Project Euler Problem 14 : longest collatz sequence

    The following iterative sequence is defined for the set of positive integers:

            𝑛 →𝑛/2 (𝑛 is even)
            𝑛 →3⁢𝑛 +1 (𝑛 is odd)

    Using the rule above and starting with 13, we generate the following sequence:
            13→40→20→10→5→16→8→4→2→1.

    It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

    Which starting number, under one million, produces the longest chain?

    NOTE: Once the chain starts the terms are allowed to go above one million.

"""

_cached_res = {1: 1}


def get_collatz_len(n):
    if n in _cached_res:
        return _cached_res[n]

    # even case
    if n % 2 == 0:
        length = 1 + get_collatz_len(n // 2)
    else:
        length = 1 + get_collatz_len(3 * n + 1)

    _cached_res[n] = length

    return length


def solve():
    max_len = 0
    final_num = 0

    for i in range(1, 1_000_000):
        curr_len = get_collatz_len(i)

        if curr_len > max_len:
            final_num = i
            max_len = curr_len

    return final_num


if __name__ == "__main__":
    print(solve())  # returns --> 837799
