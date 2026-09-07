"""
Codewars Kata: Number of trailing zeros of N! (5 kyu)
Link: https://www.codewars.com/kata/52f787eb172a8b4ae1000a34

Description:
Write a program that will calculate the number of trailing zeros in a factorial of a given number.

N! = 1 * 2 * 3 *  ... * N

Be careful 1000! has 2568 digits...
For more info, see: http://mathworld.wolfram.com/Factorial.html

Examples:
zeros(6) = 1
# 6! = 720 --> 1 trailing zero

zeros(12) = 2
# 12! = 479001600 --> 2 trailing zeros
"""


def zeros(number):
    number_of_fives = 0
    division = float("inf")
    while division > 4:
        division = number // 5
        number_of_fives += division
        number = division

    return number_of_fives


if __name__ == "__main__":
    # Test cases
    print(zeros(0))  # 0
    print(zeros(6))  # 1
    print(zeros(12))  # 2
    print(zeros(30))  # 7
