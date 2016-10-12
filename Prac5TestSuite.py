__author__ = 'mandla'
import unittest
import math
import NENE_MONGEZI_prac5 as p5

class TestPrac5Methods(unittest.TestCase):
    def test_inverse_add_vectors(self):
        self.assertEqual(p5.inverse_add_vectors([1], [2]) , [3])
        self.assertEqual(p5.inverse_add_vectors([1, 2], [1, 4]) , [5, 3])
        self.assertEqual(p5.inverse_add_vectors([1, 2, 1], [1, 4, 3]) , [4, 6, 2])

    def test_scalar_mult_matrix(self):
        self.assertEqual(p5.scalar_mult_matrix(3, []) , [])#test with 0x0 matrix
        self.assertEqual(p5.scalar_mult_matrix(5, [[2]]) , [[10]])#test with 1x1 matrix
        self.assertEqual(p5.scalar_mult_matrix(3, [[1, 0],[0,1]]) , [[3, 0],[0,3]])#test with 2x2 matrix
        self.assertEqual(p5.scalar_mult_matrix(7, [[3, 0, 5], [11, 2, 7], [4, 1, 1]]) , [[21, 0, 35], [77, 14, 49], [28, 7, 7]])#test with 3x3 matrix

    def test_distance_vectors(self):
        self.assertEqual(p5.distance_vectors([1, 1], [1, 1]) ,  0)
        self.assertEqual(p5.distance_vectors([1, 2], [1, 4]) ,  2.0)
        self.assertEqual(p5.distance_vectors([1, 2, 1], [1, 4, 3]) , math.sqrt(8))

if __name__ == '__main__':
    unittest.main()