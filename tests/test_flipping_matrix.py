import unittest
from flipping_matrix import flipping_matrix


class MyTestCase(unittest.TestCase):
    def test_flipping_matrix(self):
        test_input1 = [[1, 3], [4, 0]]
        out1 = flipping_matrix.flipping_matrix(test_input1)
        self.assertEqual(out1, 4)

        test_input2 = [[112, 42, 83, 119], [56, 125, 56, 49], [15, 78, 101, 43], [62, 98, 114, 108]]
        out2 = flipping_matrix.flipping_matrix(test_input2)
        self.assertEqual(out2, 414)


if __name__ == '__main__':
    unittest.main()
