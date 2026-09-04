"""
Codewars Kata: Find The Parity Outlier (6 kyu)
Link: https://www.codewars.com/kata/5526fc09a1bbd946250002dc

Description:
Given an array containing integers (length >= 3) where all elements are either
odd or even except for a single outlier integer N, identify and return N.

Examples:
- [2, 4, 0, 100, 4, 11, 2602, 36]  -->  11  (the only odd number)
- [160, 3, 1719, 19, 11, 13, -21] -->  160 (the only even number)
"""


def find_the_outlier(numbers: list[int]) -> int:
    if numbers[0] % 2 != numbers[1] % 2:
        if numbers[0] % 2 == numbers[2] % 2:
            return numbers[1]
        else:
            return numbers[0]

    else:
        remainder = numbers[0] % 2
        numbers = numbers[2:]
        for n in numbers:
            if n % 2 != remainder:
                return n


if __name__ == "__main__":
    print(find_the_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))  # 11
    print(find_the_outlier([160, 3, 1719, 19, 11, 13, -21]))  # 160
