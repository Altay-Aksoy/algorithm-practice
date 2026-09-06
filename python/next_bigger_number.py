"""
Codewars Kata: Next bigger number with the same digits (4 kyu)
Link: https://www.codewars.com/kata/55983863da40acbe8f000041

Description:
Create a function that takes a positive integer and returns the next bigger
number that can be formed by rearranging its digits.

Examples:
  12 ==> 21
 513 ==> 531
2017 ==> 2071

If the digits cannot be rearranged to form a bigger number, return -1:
   9 ==> -1
 111 ==> -1
 531 ==> -1
"""


def next_bigger(number: int) -> int:
    number_list = list(str(number))
    reverse_list = number_list.copy()
    reverse_list.reverse()

    for i in range(len(reverse_list)):
        last_group = reverse_list[: i + 1 :]
        if last_group == sorted(last_group):
            continue

        last_group.reverse()
        x = last_group[0]
        last_group.sort()
        lenght = len(last_group)

        for _ in range(len(last_group)):
            reverse_list.pop(0)

        for j in range(lenght):
            if last_group[j] > x:
                x = last_group.pop(j)
                last_group.sort()
                last_group.reverse()

                answer = last_group + [x] + reverse_list
                answer.reverse()
                return int("".join(answer))

    return -1


if __name__ == "__main__":
    # Test cases
    print(next_bigger(12))  # 21
    print(next_bigger(513))  # 531
    print(next_bigger(2017))  # 2071
    print(next_bigger(9))  # -1
    print(next_bigger(111))  # -1
    print(next_bigger(531))  # -1
