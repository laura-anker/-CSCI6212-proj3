# CSCI 6212 - Project 3

### Overview
This project implements an efficient polynomial algorithm, Floyd-Warshall, to calculate the diameter of a graph. The diameter is defined as the largest shortest-path distance between any pair of vertices in the graph. The code includes functions for generating a test graph, running the core algorithm, and measuring its execution time for different input sizes.

### Requirements
This code requires Python 3 and the following libraries:
- numpy <br>
To ensure you have the required libraries, you can run: pip install numpy

### How to Run
1.  **Main Analysis**: To run the experiment and measure the performance of the graph diameter calculation for various graph sizes, execute the main code:
    `python3 proj3.py`
2.  **Unit Tests**: To verify the correctness of the core function, run the unit tests:
    `python proj3test.py`

### Edge Cases Explanation:


### test_case_1_disconnected_components(self):
- This test checks how the algorithm handles a graph that contains multiple dosconnected components
- In the test case, nodes 0 and 1 are connected to each other, but node 2 is completely isolated. Since there is no path between some pairs of vertices, Floyd–Warshall leaves those distances as INF.
#### Expected behavior:
If the graph is disconnected, the diameter should be reported as INF, because at least one pair of nodes cannot reach each other.
The test accepts either:
- The largest finite distance (10), or
- INF

### test_case_2_zero_weight_cycles(self):
- This test checks how the algorithm handles zero-weight cycles.
- In the test case, the graph has two nodes: edge 0 → 1 has weight 5, edge 1 → 0 has weight −5. 
- Together, they form a cycle whose total weight is 0.
- Zero-weight cycles should not reduce any shortest-path distances.
- Floyd–Warshall correctly keeps the shortest paths as:
    0 → 1 = 5
    1 → 0 = −5
    self-distances remain 0
#### Expected behavior:
The diameter is defined as the largest finite shortest-path value, which is 5.

### test_case_3_negative_edges_no_cycle(self):
- This test verifies correct behavior when the graph contains negative edge weights, but no negative-weight cycle.
- In the test graph, there is a negative edge (1 → 2 = −5), but no sequence of edges creates a cycle with negative total cost. One node remains unreachable. Floyd–Warshall fully supports negative edges, as long as no negative cycle exists.
#### Expected behavior:
Since one vertex is unreachable from others, the diameter should be returned as INF (here represented as 1000).
    
### Function Descriptions
The code is organized into four main functions: floyd_warshall, graph_diameter, generate_graph, and main.

### floyd_warshall(g): 
    Purpose: To compute the shortest path between all pairs of vertices in a given graph matrix. It implements the Floyd-Warshall algorithm, which has a time complexity of O(n^3), where n is the number of vertices.
    Parameters:g: A 2D numpy array (matrix) where g[i][j] represents the initial distance (weight) of the edge from vertex i to vertex j. A very large value (maxVal = 1000000000) is used to signify no direct edge.
    Process: It iterates through all vertices k (the intermediate vertex) and then updates the shortest path between every pair (i, j) using the formula: g[i][j] = min(g[i][j], g[i][k] + g[k][j])
    Returns: This function returns nothing (None) but modifies the input matrix g in place so that g[i][j] holds the shortest path distance.
    
### graph_diameter(g):
    Purpose: To find the diameter of the graph, which is the maximum shortest-path distance between any pair of vertices.
    Parameters:g: A 2D numpy array representing the graph's initial edge distances.
    Process: It first calls floyd_warshall(g) to populate the matrix with all-pairs shortest path distances. It then iterates through the resulting distance matrix to find the largest value, which is the graph's diameter.
    Returns: An integer representing the graph diameter.
    
### generate_graph(n):
    Purpose: To create a randomized n times n adjacency matrix representing a weighted graph for testing purposes.
    Parameters:n: An integer representing the number of vertices in the graph.
    Process: Creates an n times n matrix initialized with zeros. For non-diagonal elements, there is an 80% probability (edge_probability = 0.8) of setting the edge weight to a random integer between 1 and 100. The remaining 20% of edges are set to the large value (maxVal), indicating no direct connection. Diagonal elements are set to 0.
    Returns: A 2D numpy array representing the generated graph.

### perform_experimental_analysis(n_values):
    Purpose: This function iterates through a provided list of input sizes (n_values). 
    Parameters: n_values - list of input sizes
    Process: For each size n, it
        - Generates a random weighted graph using generate_graph(n)
        - Starts a timer using time.time()
        - Executes the graph_diameter function (which runs the core Floyd-Warshall logic)
        - Stops the timer to capture the exact runtime
        - Calculates the theoretical operation count n^3
        - Aggregates these metrics into a structured list of dictionaries, which is returned for further processing (table and plotting)

### main():
    Purpose: To run the performance test on the graph_diameter function for various graph sizes.
    Process: Defines a set of test sizes for the number of vertices: ns = [5, 10, 15, 50, 100, 200]. For each n, it generates a graph using generate_graph(n). It measures the time taken to run graph_diameter on a copy of the matrix. It prints the execution time for each input size n.
    Expected Output: The program will print the execution time for each test case, demonstrating the polynomial time complexity of the algorithm as the number of vertices n increases
