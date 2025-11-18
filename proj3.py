import time
import numpy as np
import random
import pandas as pd 
import matplotlib.pyplot as plt

'''Diameter of a graph is defined as the largest distance between any pair of vertices 
of G.  Give an efficient polynomial algorithm to find the diameter of the graph.'''

# Define infinity constant
#max value representing infinity (no edge)
INF = 1000000000

#given matrix representing distance between vetices in graph (format described in generate_graph)
#alters the given matrix so each spot in matrix [i, j] represents shortest path from i to j
def floyd_warshall(g):
    '''
    Computes all-pairs shortest paths in graph g using the Floyd-Warshall algorithm
    '''
    #n = number of vertices
    n = len(g)
    #Select each vertex k to be an intermediate vertex (Outer loop: O(n))
    for k in range(n):
        #iterate through each pair of vertices, (Middle loop: O(n))
        for i in range(n):
            #(Inner loop: O(n))
            for j in range(n):
                #if i and j are reachable by intermediate vertex k
                if (g[i][k] != INF and g[k][j] != INF):
                    #let min distance from i to j be itself or smaller path found with intermediate
                    g[i][j] = min(g[i][j], (g[i][k] + g[k][j]))
    return

#returns the largest distance between any pair of vertices in graph g, represented as matrix described in generate_graph
def graph_diameter(g):
    maxDist = 0
    g_copy = g.copy()
    #call floyd-warshall on g
    floyd_warshall(g_copy)
    #find max value in resulting matrix
    for i in range(len(g_copy)):
        for j in range(len(g_copy)):
            if (g_copy[i][j] > maxDist):
                maxDist = g_copy[i][j]
    #max value is graph diameter
    return maxDist

#generates a nxn matrix representing a graph. Each value [i][j] in the matrix represents the distance between vertices i and j
#values on the diagonal must be 0 because distance from node to itself is 0. 
#0.2 probability of edge being set to extremely high value to represent nodes that are not connected to each other
def generate_graph(n):
    edge_probability = 0.8 #probability of an edge being set between 2 nodes
    matrix = np.zeros((n, n))#create nxn matrix full of 0s
    #iterate through each element
    for i in range(n):
        for j in range(n):
            # Distance from node to itself is 0
            if i == j:
                matrix[i][j] = 0
            #if not diagonal element
            else:
                #set some random edges to max
                if random.random() < edge_probability:
                    #set most edges to weights between 1 and 100
                    matrix[i][j] = random.randint(1, 100)
                else:
                    matrix[i][j] = INF
    return matrix

def perform_experimental_analysis(n_values):
    """Runs the experiment for a list of n values and collects data"""
    results = []
    
    for n in n_values:
        # Generate the graph for the current n
        matrix = generate_graph(n)
        
        # Measure execution time
        start_time = time.time()
        graph_diameter(matrix)
        end_time = time.time()
        
        runtime = end_time - start_time
        n_cubed = n**3
        
        results.append({
            'n': n, 
            'runtime': runtime, 
            'n_cubed': n_cubed
        })
        
    return pd.DataFrame(results)

def main():
    #define a larger range of inputs for better analysis stability (N values >= 100 are most important)
    N_VALUES = [10, 30, 60, 90, 120, 150, 200, 250, 300]
    
    print("--- Running Experimental Analysis for Floyd-Warshall (O(n^3)) ---")
    data_list = perform_experimental_analysis(N_VALUES)
    
    
    #Find the scaling constant C using the largest value (n_max)
    n_max_data = data_list.iloc[-1]
    n_max = n_max_data['n']
    runtime_max = n_max_data['runtime']
    n_cubed_max = n_max_data['n_cubed']
    
    #Calculate scaling constant C
    C = runtime_max / n_cubed_max
    
    print(f"\nScaling Constant C (Derived from n={n_max}): {C:.8e}")
    
    #formatt data
    final_data = []
    for data in data_list.itertuples(index=False):
        n_cubed = data.n_cubed
        runtime = data.runtime
        c_point = runtime / n_cubed
        adjusted_theoretical = n_cubed * C

        final_data.append({
            'n': data.n,
            'n_cubed': n_cubed,
            'runtime': runtime,
            'c_point': c_point,
            'adjusted_theoretical': adjusted_theoretical
        })

    
    print("\n---Numerical Data ---")
    
    #widths for manual Markdown table
    col_widths = [8, 18, 20, 25, 20]
    
    # Headers
    header = ["n", "n^3 (Theoretical)", "Experimental Time (s)", "Scaling Constant C", "Adjusted Theoretical (s)"]
    print("| " + " | ".join(h.ljust(w) for h, w in zip(header, col_widths)) + " |")
    print("|" + "|".join("-" * (w + 2) for w in col_widths) + "|")
    
    # Print data rows
    for data in final_data:
        row = [
            f"{data['n']}".ljust(col_widths[0]),
            f"{data['n_cubed']:,.0f}".ljust(col_widths[1]),
            f"{data['runtime']:.6f}".ljust(col_widths[2]),
            f"{data['c_point']:.8e}".ljust(col_widths[3]),
            f"{data['adjusted_theoretical']:.6f}".ljust(col_widths[4])
        ]
        print("| " + " | ".join(row) + " |")


    # Generate Plot
    # Extract data for plotting
    x_axis_values = [data['n_cubed'] for data in final_data]
    experimental_costs = [data['runtime'] for data in final_data]
    theoretical_adjusted = [data['adjusted_theoretical'] for data in final_data]

    # Create the plot
    plt.figure(figsize=(10, 6))
    
    # Plot experimental data
    plt.plot(x_axis_values, experimental_costs, 'bo-', label='Experimental Runtime')
    
    # Plot adjusted theoretical baseline
    plt.plot(x_axis_values, theoretical_adjusted, 'r--', label='Adjusted Theoretical (C * n^3)')
    
    plt.xlabel('n^3 (Theoretical Operation)')
    plt.ylabel('Runtime (Seconds)')
    plt.title('Experimental vs. Adjusted Theoretical Time Complexity for Floyd-Warshall')
    plt.grid(True)
    plt.legend()
    plt.show()



if __name__ == "__main__":
    main()
