"""
Codewars Kata: Calculating with Functions (5 kyu)
Link: https://www.codewars.com/kata/525f3ed15025e45073000495

Description:
This time we want to write calculations using functions and get the results.
Requirements:
- There must be a function for each number from 0 ("zero") to 9 ("nine").
- There must be a function for each of the following mathematical operations:
  plus, minus, times, divided_by.
- Each calculation consists of exactly one operation and two numbers.
- The most outer function represents the left operand, the most inner function represents the right operand.
- Division should be integer division.

Examples:
seven(times(five())) # 35
four(plus(nine())) # 13
eight(minus(three())) # 5
six(divided_by(two())) # 3
"""

# ==============================================================================
# New Solution (Functions returning closures)
# ==============================================================================


# Operation Functions
def plus(num2):
    return lambda num1: num1 + num2


def minus(num2):
    return lambda num1: num1 - num2


def times(num2):
    return lambda num1: num1 * num2


def divided_by(num2):
    return lambda num1: num1 // num2


# Number Functions
def zero(operation=lambda num1: num1):
    return operation(0)


def one(operation=lambda num1: num1):
    return operation(1)


def two(operation=lambda num1: num1):
    return operation(2)


def three(operation=lambda num1: num1):
    return operation(3)


def four(operation=lambda num1: num1):
    return operation(4)


def five(operation=lambda num1: num1):
    return operation(5)


def six(operation=lambda num1: num1):
    return operation(6)


def seven(operation=lambda num1: num1):
    return operation(7)


def eight(operation=lambda num1: num1):
    return operation(8)


def nine(operation=lambda num1: num1):
    return operation(9)


# ==============================================================================
# Old Solution (Decorators and global state)
# ==============================================================================
#
# operation_list = []
# operation = ""
#
#
# def is_it_three(func):
#     def inner(*args, **kwargs):
#         global operation
#
#         # Before FNC
#
#         # FNC
#         res = func(*args, **kwargs)
#
#         # After FNC
#         if len(operation_list) == 2:
#             num1 = operation_list[1]
#             num2 = operation_list[0]
#             op = operation
#
#             # Bir sonraki işlem için temizlik
#             operation_list.clear()
#             operation = ""
#
#             if op == "+":
#                 return num1 + num2
#             elif op == "-":
#                 return num1 - num2
#             elif op == "*":
#                 return num1 * num2
#             elif op == "/":
#                 return num1 // num2
#         else:
#             return res
#
#     return inner
#
#
# @is_it_three
# def zero(a=None):
#     operation_list.append(0)
#
#
# @is_it_three
# def one(a=None):
#     operation_list.append(1)
#
#
# @is_it_three
# def two(a=None):
#     operation_list.append(2)
#
#
# @is_it_three
# def three(a=None):
#     operation_list.append(3)
#
#
# @is_it_three
# def four(a=None):
#     operation_list.append(4)
#
#
# @is_it_three
# def five(a=None):
#     operation_list.append(5)
#
#
# @is_it_three
# def six(a=None):
#     operation_list.append(6)
#
#
# @is_it_three
# def seven(a=None):
#     operation_list.append(7)
#
#
# @is_it_three
# def eight(a=None):
#     operation_list.append(8)
#
#
# @is_it_three
# def nine(a=None):
#     operation_list.append(9)
#
#
# def plus(num):
#     global operation
#     operation = "+"
#
#
# def minus(num):
#     global operation
#     operation = "-"
#
#
# def times(num):
#     global operation
#     operation = "*"
#
#
# def divided_by(num):
#     global operation
#     operation = "/"

# ==============================================================================
# Driver & Tests
# ==============================================================================
if __name__ == "__main__":
    print(seven(times(five())))  # 35
    print(four(plus(nine())))  # 13
    print(eight(minus(three())))  # 5
    print(six(divided_by(two())))  # 3
    print(one(times(zero())))  # 0
