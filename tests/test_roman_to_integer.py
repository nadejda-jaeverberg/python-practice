import unittest
from roman_numerals import roman_to_integer


class MyTestCase(unittest.TestCase):
    def test_roman_to_int(self):
        s1 = "III"
        exp1 = 3
        out1 = roman_to_integer.roman_to_int(s1)
        self.assertEqual(out1, exp1)

        with self.assertRaises(ValueError) as cm:
            roman_to_integer.roman_to_int(9)
        self.assertEqual(
            "Expecting a string input",
            str(cm.exception)
        )

        with self.assertRaises(ValueError) as cm:
            roman_to_integer.roman_to_int("0gfRTIXMDV")
        self.assertEqual(
            "Expecting a string input with only following symbols: ('I', 'V', 'X', 'L', 'C', 'D', 'M')",
            str(cm.exception)
        )

        s2 = "LVIII"
        exp2 = 58
        out2 = roman_to_integer.roman_to_int(s2)
        self.assertEqual(out2, exp2)

        s3 = "MCMXCIV"
        exp3 = 1994
        out3 = roman_to_integer.roman_to_int(s3)
        self.assertEqual(out3, exp3)


if __name__ == '__main__':
    unittest.main()
