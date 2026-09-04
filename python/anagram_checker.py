# Check the word whether it is anagram or not!
# Anagram: The word which letters are same with another word but the sorting is different


def is_anagram(word1: str, word2: str) -> bool:
    word1 = word1.lower().replace(" ", "")
    word2 = word2.lower().replace(" ", "")

    return sorted(word1) == sorted(word2)


if __name__ == "__main__":
    test_cases = [
        ("listen", "silent"),  # True
        ("elbow", "below"),  # True
        ("Dormitory", "Dirty room"),  # True
        ("hello", "world"),  # False
        ("python", "typhon"),  # True
        ("apple", "pale"),  # False
    ]
    for w1, w2 in test_cases:
        print(
            f"{w1} and {w2} are ANAGRAM"
            if is_anagram(w1, w2)
            else f"{w1} and {w2} are NOT ANAGRAM"
        )
