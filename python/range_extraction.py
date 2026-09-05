"""
Codewars Kata: Range Extraction (4 kyu)
Link: https://www.codewars.com/kata/51ba717bb08c1cd60f00002f

Description:
A format for expressing an ordered list of integers is to use a comma separated list of either:
- individual integers
- or a range of integers denoted by the starting integer separated from the end integer in the range by a dash, '-'.
The range includes all integers in the interval including both endpoints.
It is not considered a range unless it spans at least 3 numbers.
"""


def solution(args: list) -> str:
    answer = ""
    while args != []:
        n1 = args[0] - 1
        num_list = []
        for arg in args:
            if arg - 1 == n1:
                n1 += 1
                num_list.append(arg)
                if num_list[-1] == args[-1]:
                    for _ in range(len(num_list)):
                        args.pop(0)
                    break
            else:
                for _ in range(len(num_list)):
                    args.pop(0)
                break
        if len(num_list) == 1:
            answer += str(num_list[0]) + ","
        elif len(num_list) == 2:
            answer += ",".join([str(num_list[0]), str(num_list[1])]) + ","
        else:
            answer += "-".join([str(num_list[0]), str(num_list[-1])]) + ","

    return answer.removesuffix(",")


if __name__ == "__main__":
    test_data = [
        -10,
        -9,
        -8,
        -6,
        -3,
        -2,
        -1,
        0,
        1,
        3,
        4,
        5,
        7,
        8,
        9,
        10,
        11,
        14,
        15,
        17,
        18,
        19,
        20,
    ]
    print(solution(test_data))
    # Output: -10--8,-6,-3-1,3-5,7-11,14,15,17-20
