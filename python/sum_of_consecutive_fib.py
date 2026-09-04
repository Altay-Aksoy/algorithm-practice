"""
Codewars Kata: Product of consecutive Fib numbers (5 kyu)
Link: https://www.codewars.com/kata/5541f58fa94456e5110001a4

Description:
Given an integer prod, find two consecutive Fibonacci numbers F(n) and F(n+1)
such that F(n) * F(n+1) = prod.

If found, return [F(n), F(n+1), True].
If not, return [F(n), F(n+1), False] where F(n) * F(n+1) > prod and F(n-1) * F(n) < prod.
"""


def product_fib(_prod) -> list:
    n1, n2 = 0, 1
    while n1 * n2 < _prod:
        n1, n2 = (n2, n1 + n2)
    return [n1, n2, n1 * n2 == _prod]


if __name__ == "__main__":
    # Test cases
    print(product_fib(4895))  # [55, 89, True]
    print(product_fib(5895))  # [89, 144, False]
    print(product_fib(74049690))  # [6765, 10946, True]
    print(product_fib(84049690))  # [10946, 17711, False]
