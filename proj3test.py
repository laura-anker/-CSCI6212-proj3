import unittest
from proj3 import graph_diameter, INF
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

#EDGES CASES 1 - 4 BELOW
    def test_case_1_disconnected_components(self):
        """
        Case 1: Disconnected Graphs.
        Scenario: Two components with no path between them
        """
        maxVal = INF
        # Component 1: 0 <-> 1 (weight 10)
        # Component 2: 2 (isolated)
        a = np.array([
            [0,   10,  maxVal],
            [10,  0,   maxVal],
            [maxVal, maxVal, 0  ]
        ], dtype=float)
        

        result = graph_diameter(a.copy())
        
        # Check if result is either 10 (max finite) or INF (disconnected)
        self.assertTrue(result == 10 or result == maxVal)

    def test_case_2_zero_weight_cycles(self):
        """
        Case 2: Zero-Weight Cycles.
        Scenario: 0 -> 1 (5) and 1 -> 0 (-5). Sum is 0
        """
        a = np.array([
            [0,   5],
            [-5,  0]
        ], dtype=float)
        
        # Shortest paths:
        # 0->0: 0 
        # 0->1: 5
        # 1->0: -5
        # 1->1: 0
        # Max distance in matrix is 5.
        expected = 5
        result = graph_diameter(a.copy())
        self.assertEqual(result, expected)

    def test_case_3_negative_edges_no_cycle(self):
        """
        Case 3: Negative Edge Weights (Without Negative Cycles).
        """
        maxVal = 1000
        a = np.array([
            [0,      10,  maxVal],
            [maxVal, 0,   -5    ],
            [maxVal, maxVal, 0  ]
        ], dtype=float)
        
        expected = 1000
        result = graph_diameter(a.copy())
        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
