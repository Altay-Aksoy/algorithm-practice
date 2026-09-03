import string


def isPalindrome(txt: str) -> bool:
    txt = txt.replace(" ", "").lower()
    for p in string.punctuation:
        txt = txt.replace(p, "")

    txt_rev = txt[::-1]

    return txt == txt_rev


if __name__ == "__main__":
    testler = ["racecar", "hello", "kayak"]
    for t in testler:
        print(f"{t} -> {isPalindrome(t)}")
