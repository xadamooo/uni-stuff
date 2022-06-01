import numpy
import unittest
import scipy
import scipy.linalg

'''zad3'''


class MatrixTests(unittest.TestCase):

    def setUp(self):
        self.matrix_test = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        (P, L, U) = scipy.linalg.lu(numpy.transpose(self.matrix_test))

    def test_made_of_numbers(self):
        num = True
        for x in self.matrix_test:
            for y in x:
                try:
                    int_value = int(y)
                except ValueError:
                    num = False
                else:
                    del(int_value)
        self.assertTrue(num, 'bledne dane')

    def test_if_square(self):
        rows = len(self.matrix_test)
        columns = len(self.matrix_test[0])
        self.assertEqual(rows, columns, 'macierz nie jest kwadratowa')

    def test_is_invertible(self):
        det = numpy.linalg.det(self.matrix_test)
        self.assertNotEqual(det, 0, 'wyznacznik rowny 0')


if __name__ == '__main__':
    unittest.main()
