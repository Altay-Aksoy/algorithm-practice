"""
Codewars Kata: Count IP Addresses (5 kyu)
Link: https://www.codewars.com/kata/526989a48f71e6daec000880

Description:
Implement a function that receives two IPv4 addresses, and returns the number
of addresses between them (including the first one, excluding the last one).

All inputs will be valid IPv4 addresses in the form of strings.
The last address will always be greater than the first one.
"""


def ips_between(start: str, end: str) -> int:
    start_list = start.split(".")
    end_list = end.split(".")

    return (
        (int(end_list[0]) - int(start_list[0])) * (256**3)
        + (int(end_list[1]) - int(start_list[1])) * (256**2)
        + (int(end_list[2]) - int(start_list[2])) * (256**1)
        + int(end_list[3])
        - int(start_list[3])
    )


if __name__ == "__main__":
    # Test cases
    print(ips_between("10.0.0.0", "10.0.0.50"))  # 50
    print(ips_between("10.0.0.0", "10.0.1.0"))  # 256
    print(ips_between("20.0.0.10", "20.0.1.0"))  # 246
