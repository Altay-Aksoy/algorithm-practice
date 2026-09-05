"""
Codewars Kata: Integers: Recreation One (5 kyu)
Link: https://www.codewars.com/kata/55aa075506463dac660001c2

Description:
Find all integers between m and n (m and n integers with 1 <= m <= n) such that
the sum of their squared divisors is itself a square.
"""

import math


def find_divisors_sum(number: int) -> int:
    summary = 0
    for j in range(1, math.isqrt(number) + 1):
        if number % j == 0:
            summary += j**2
            if j != number // j:
                summary += (number // j) ** 2
    return summary


def list_squared(m: int, n: int) -> list:
    pairs = []
    for i in range(m, n + 1):
        sum_of = find_divisors_sum(i)
        if math.sqrt(sum_of).is_integer():
            pairs.append([i, sum_of])
    return pairs


if __name__ == "__main__":
    # Test cases
    print(list_squared(1, 250))    # [[1, 1], [42, 2500], [246, 84100]]
    print(list_squared(42, 250))   # [[42, 2500], [246, 84100]]
    print(list_squared(250, 500))  # [[287, 84100]]
