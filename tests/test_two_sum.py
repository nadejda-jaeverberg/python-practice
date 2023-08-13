import unittest
from add_two_numbers import two_sum


class MyTestCase(unittest.TestCase):
    def test_two_sum(self):
        list_in1 = [2, 7, 11, 15]
        target1 = 9

        list_in2 = [3, 2, 4]
        target2 = 6

        list_in3 = [3, 3]
        target3 = 6

        out1 = two_sum.two_sum(list_in1, target1)
        self.assertListEqual(out1, [0, 1])

        out2 = two_sum.two_sum(list_in2, target2)
        self.assertListEqual(out2, [1, 2])

        out3 = two_sum.two_sum(list_in3, target3)
        self.assertListEqual(out3, [0, 1])

        out4 = two_sum.two_sum(list_in1, "a")
        self.assertEqual(out4, None)

        out5 = two_sum.two_sum([1, 2, 3, "n", 7], 0)
        self.assertEqual(out5, None)

        out6 = two_sum.two_sum([1, 1], 8)
        self.assertEqual(out6, None)


if __name__ == '__main__':
    unittest.main()
