"""
Codewars Kata: What's a Perfect Power anyway? (5 kyu)
Link: https://www.codewars.com/kata/54d4c8b08845f8d694000592

Description:
A perfect power is a classification of positive integers:
In mathematics, a perfect power is a positive integer that can be expressed as an
integer power of another positive integer. More formally, n is a perfect power
if there exist natural numbers m > 1, and k > 1 such that m**k = n.

Your task is to check whether a given integer is a perfect power.
If it is a perfect power, return a pair [m, k] with m**k = n and m > 1, k > 1.
If not, return None.
"""

import math


# ==============================================================================
# Optimal Approach: Exponent Search with Logarithmic Bound — O(log N)
# ==============================================================================
def isPP(number: int) -> list[int] | None:
    for num in range(2, int(math.log2(number)) + 1):
        root = round(number ** (1 / num))
        if root**num == number:
            return [root, num]
    return None


# ==============================================================================
# Initial Working Approach: Base Search via Trial Division — O(sqrt(N))
# ==============================================================================
def isPP_alternative(number: int) -> list[int] | None:
    for i in range(2, int(math.sqrt(number)) + 1):
        num_copy = number
        counter = 0
        while num_copy > 1:
            if num_copy % i != 0:
                break
            else:
                num_copy //= i
                counter += 1
        else:
            return [i, counter]
    return None


# ==============================================================================
# Driver & Tests
# ==============================================================================
if __name__ == "__main__":
    # Optimal approach tests
    print("Optimal Approach:")
    print(isPP(4))  # [2, 2]
    print(isPP(9))  # [3, 2]
    print(isPP(5))  # None
    print(isPP(81))  # [9, 2] veya [3, 4]

    # Initial approach tests
    print("\nInitial Alternative:")
    print(isPP_alternative(4))  # [2, 2]
    print(isPP_alternative(9))  # [3, 2]
    print(isPP_alternative(5))  # None
