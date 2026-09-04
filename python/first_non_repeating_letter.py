"""
Codewars Kata: First non-repeating character (5 kyu)
Link: https://www.codewars.com/kata/52bc7447ac3f938b3700046e

Description:
Write a function named first_non_repeating_letter that takes a string input,
and returns the first character that is not repeated anywhere in the string.

For example, if given the input 'stress', the function should return 't',
since the letter t only occurs once in the string, and occurs first in the string.

As an added challenge, upper- and lowercase letters are considered the same
character, but the function should return the correct initial case for the
initial letter.
"""


def first_non_repeating_letter(txt: str) -> str:
    lower_txt = txt.lower()
    letters, repeated_letters = [], set()
    for letter in lower_txt:
        if letter in repeated_letters:
            continue
        if letter in letters:
            letters.remove(letter)
            repeated_letters.add(letter)
        else:
            letters.append(letter)

    return txt[lower_txt.index(letters[0])] if letters else ""


if __name__ == "__main__":
    # Test cases
    print(first_non_repeating_letter("stress"))  # "t"
    print(first_non_repeating_letter("sTreSS"))  # "T"
    print(first_non_repeating_letter("moonmen"))  # "e"
    print(first_non_repeating_letter(""))  # ""
