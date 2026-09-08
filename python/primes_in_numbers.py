"""
Codewars Kata: Primes in numbers (5 kyu)
Link: https://www.codewars.com/kata/54d512e62a5e54c96200019e

Description:
Given a positive number n > 1 find the prime factor decomposition of n.
The result will be a string with the following form:
"(p1**n1)(p2**n2)...(pk**nk)"
with the p(i) in increasing order and n(i) empty if n(i) == 1.

Example: n = 86240 should return "(2**5)(5)(7**2)(11)"
"""

# ==============================================================================
# Helper / Alternative Idea
# ==============================================================================
# import math
# def find_next_prime(prime: int) -> int:
#     isPrime = True
#     while isPrime:
#         prime += 1
#         for i in range(2, int(math.sqrt(prime)) + 1):
#             if prime % i == 0:
#                 break
#         else:
#             isPrime = False
#     return prime


# ==============================================================================
# Solution
# ==============================================================================
def prime_factors(number):
    # Calculate the divisiors
    num = 2
    primes_dict = {}
    answer = ""
    counter = 0
    while True:
        if number % num == 0:
            number //= num
            counter += 1
            if number == 1:
                primes_dict.update({num: counter})
                break
        else:
            if counter != 0:
                primes_dict.update({num: counter})
                counter = 0
            num += 1
            if num**2 > number:
                primes_dict.update({number: 1})
                break

    # Convert to the demanded string
    for k, v in primes_dict.items():
        if v != 1:
            answer += f"({k}**{v})"
        else:
            answer += f"({k})"

    return answer


# ==============================================================================
# Driver & Tests
# ==============================================================================
if __name__ == "__main__":
    print(prime_factors(86240))  # (2**5)(5)(7**2)(11)
    print(prime_factors(7775460))  # (2**2)(3**3)(5)(7)(11**2)(17)
    print(prime_factors(7919))  # (7919)
