"""
Codewars Kata: Perimeter of squares in a rectangle (5 kyu)
Link: https://www.codewars.com/kata/559a28007caad2ac4e000083

Description:
The drawing shows 6 squares the sides of which have a length of 1, 1, 2, 3, 5, 8.
It's easy to see that the sum of the perimeters of these squares is:
4 * (1 + 1 + 2 + 3 + 5 + 8) = 4 * 20 = 80.

Could you give the sum of the perimeters of all the squares in a rectangle
when there are n + 1 squares disposed in the same manner as in the drawing?
"""

# ==============================================================================
# Optimal Solution: O(N) Time, O(1) Space
# ==============================================================================


def perimeter(number: int) -> int:
    n1, n2, total = 1, 1, 1
    for _ in range(number):
        total += n2
        n1, n2 = n2, n1 + n2
    return total * 4


# ==============================================================================
# Alternative Solution: O(N) Time, O(N) Space
# ==============================================================================

# def perimeter(number: int) -> int:
#     fib_nums = [0, 1]

#     for _ in range(number):
#         fib_nums.append(fib_nums[-1] + fib_nums[-2])

#     return sum(fib_nums) * 4


# ==============================================================================
# Driver & Tests
# ==============================================================================
if __name__ == "__main__":
    # Test cases
    print(perimeter(5))  # 80
    print(perimeter(7))  # 216
    print(perimeter(20))  # 114624
