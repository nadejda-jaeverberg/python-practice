"""
Roman to integer task from leetcode, see README.md for details

Date: 5th of May 2022
Author: Nadejda Jaeverberg
"""


def roman_to_int(s: str) -> int:
    """
    Take a string that is guaranteed to be a Roman number as per contraints and turn it into integer
    :param s: string containing Roman number
    :return: integer
    """
    # Do a simple check of the input, it must be a string! and
    # must contain only: ('I', 'V', 'X', 'L', 'C', 'D', 'M')
    if not isinstance(s, str):
        print(f"Wrong input, expecting a string and received: {s} with type: {type(s)}")
        raise ValueError("Expecting a string input")

    check_string = [elem for elem in s if elem not in ('I', 'V', 'X', 'L', 'C', 'D', 'M')]
    if len(check_string) > 0:
        print(f"Wrong input, expecting a string with only the following symbols: "
              f"('I', 'V', 'X', 'L', 'C', 'D', 'M') and received: {s} with symbols that "
              f"don't match the criteria: {check_string}")
        raise ValueError("Expecting a string input with only following symbols: ('I', 'V', 'X', 'L', 'C', 'D', 'M')")

    # Declaring a dictionary for Roman numerals for easy lookup
    roman = {"I": 1,
             "V": 5,
             "X": 10,
             "L": 50,
             "C": 100,
             "D": 500,
             "M": 1000
             }

    # Initialise the sum
    out_sum = 0
    print(f"Input string: {s}")

    # Walk through the string with Roman numeral
    for i in range(len(s) - 1):
        print(f"elem: {s[i]} with value: {roman[s[i]]}")
        print(f"Next elem: {s[i + 1]} with value: {roman[s[i + 1]]}")

        # Check the order of the letters - if smaller or equal number follows a bigger number then add
        if roman[s[i]] >= roman[s[i + 1]]:
            out_sum += roman[s[i]]
        # Else substract
        else:
            out_sum -= roman[s[i]]

    return out_sum + roman[s[-1]]
