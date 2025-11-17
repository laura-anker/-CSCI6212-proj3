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

### Function Descriptions
The code is organized into four main functions: floyd_warshall, graph_diameter, generate_graph, and main.

### floyd_warshall(g): 
    Purpose: To compute the shortest path between all pairs of vertices in a given graph matrix. It implements the Floyd-Warshall algorithm, which has a time complexity of O(n^3), where n is the number of vertices.
    Parameters:g: A 2D numpy array (matrix) where g[i][j] represents the initial distance (weight) of the edge from vertex i to vertex j. A very large value (maxVal = 1000000000) is used to signify no direct edge.
    Process: It iterates through all vertices k (the intermediate vertex) and then updates the shortest path between every pair (i, j) using the formula:g[i][j] = \min(g[i][j], g[i][k] + g[k][j])
    Returns: This function returns nothing (None) but modifies the input matrix g in place so that g[i][j] holds the shortest path distance.
    
### graph_diameter(g):
    Purpose: To find the diameter of the graph, which is the maximum shortest-path distance between any pair of vertices.
    Parameters:g: A 2D numpy array representing the graph's initial edge distances.
    Process:It first calls floyd_warshall(g) to populate the matrix with all-pairs shortest path distances.It then iterates through the resulting distance matrix to find the largest value, which is the graph's diameter.
    Returns: An integer representing the graph diameter.
    
### generate_graph(n):
    Purpose: To create a randomized n \times n adjacency matrix representing a weighted graph for testing purposes.
    Parameters:n: An integer representing the number of vertices in the graph.
    Process:Creates an n \times n matrix initialized with zeros.For non-diagonal elements, there is an 80\% probability (edge_probability = 0.8) of setting the edge weight to a random integer between 1 and 100.The remaining 20\% of edges are set to the large value (maxVal), indicating no direct connection. Diagonal elements are set to 0.
    Returns: A 2D numpy array representing the generated graph.

### main():
    Purpose: To run the performance test on the graph_diameter function for various graph sizes.
    Process:Defines a set of test sizes for the number of vertices: ns = [5, 10, 15, 50, 100, 200].For each n, it generates a graph using generate_graph(n).It measures the time taken to run graph_diameter on a copy of the matrix. It prints the execution time for each input size n.
    Expected Output: the program will print the execution time for each test case, demonstrating the polynomial time complexity of the algorithm as the number of vertices n increases
