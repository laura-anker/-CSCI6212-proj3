import unittest
from proj3 import graph_diameter
import numpy as np

class TestGraphDiameter(unittest.TestCase):
    #edge test with two nodes
    def test_1(self):
        a = np.array([[0, 1], [1, 0]])
        expected = 1
        result = graph_diameter(a.copy()) 
        self.assertEqual(result, expected)

    #simple directed, weighted test
    def test_2(self):
        maxVal = 1000000000
        a = np.array([[0, 4, maxVal, 8, maxVal], 
                      [maxVal, 0, 1, maxVal, 6], 
                      [2, maxVal, 0, 3, maxVal], 
                      [maxVal, maxVal, 1, 0, 2], 
                      [2, maxVal, maxVal, 5, 0]])
        expected = 10
        result = graph_diameter(a.copy()) 
        self.assertEqual(result, expected)

    #simple directed, unweighted test
    def test_3(self):
        maxVal = 1000000000
        a = np.array([[0, 1, maxVal, 1, maxVal], 
                    [maxVal, 0, 1, maxVal, 1], 
                    [1, maxVal, 0, 1, maxVal], 
                    [maxVal, maxVal, 1, 0, 1], 
                    [1, maxVal, maxVal, 1, 0]])
        expected = 3
        result = graph_diameter(a.copy()) 
        self.assertEqual(result, expected)

    #simple undirected, unweighted test
    def test_4(self):
        maxVal = 1000000000
        a = np.array([[0, 1, 1, 1], 
                    [1, 0, maxVal, 1], 
                    [1, maxVal, 0, 1], 
                    [1, 1, 1, 0]])
        expected = 2
        result = graph_diameter(a.copy()) 
        self.assertEqual(result, expected)

     #simple undirected, weighted test
    def test_5(self):
        maxVal = 1000000000
        a = np.array([[0, 2, 1, 5], 
                    [2, 0, maxVal, 1], 
                    [1, maxVal, 0, 100], 
                    [5, 1, 100, 0]])
        expected = 4
        result = graph_diameter(a.copy()) 
        self.assertEqual(result, expected)

    #directed, weighted test with unconnected graph
    def test_6(self):
        maxVal = 1000000000
        a = np.array([[0, 4, maxVal, 8, maxVal, maxVal], 
                      [maxVal, 0, 1, maxVal, 6, maxVal], 
                      [2, maxVal, 0, 3, maxVal, maxVal], 
                      [maxVal, maxVal, 1, 0, 2, maxVal], 
                      [2, maxVal, maxVal, 5, 0, maxVal], 
                      [maxVal, maxVal, maxVal, maxVal, maxVal, 0]])
        expected = maxVal
        result = graph_diameter(a.copy()) 
        self.assertEqual(result, expected)

    #directed, weighted test with nagative values
    def test_7(self):
        maxVal = 1000000000
        a = np.array([[0, -4, maxVal, 8, maxVal], 
                      [maxVal, 0, 1, maxVal, -6], 
                      [2, maxVal, 0, 3, maxVal], 
                      [maxVal, maxVal, 1, 0, -2], 
                      [2, maxVal, maxVal, 5, 0]])
        expected = -8
        result = graph_diameter(a.copy()) 
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main()
