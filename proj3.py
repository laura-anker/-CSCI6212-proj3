import time
import numpy as np
import random

'''Diameter of a graph is defined as the largest distance between any pair of vertices 
of G.  Give an efficient polynomial algorithm to find the diameter of the graph.'''

def floyd_warshall(g):
    #do stuff
    return

#returns the largest distance between any pair of vertices in graph g, represented as matrix describes in generate_graph
def graph_diameter(g):
    maxDist = -100
    #call floyd-warshall on g
    floyd_warshall(g)
    #find max value in resulting matrix
    for i in range(len(g)):
        for j in range(len(g)):
            if (g[i][j] > maxDist):
                maxDist = g[i][j]
    #max value is graph diameter
    return maxDist

#generates a nxn matrix representing a graph. Each value [i][j] in the matrix represents the distance between vertices i and j
#values on the diagonal must be 0 because distance from node to itself is 0. 
#0.8 probability of edge being set to extremely high value to represent nodes that are not connected to each other
def generate_graph(n):
    maxVal = 1000000000 #effectively infinite
    edge_probability = 0.8 #probability of an edge being set between 2 nodes
    matrix = np.zeros((n, n))#create nxn matrix full of 0s
    #iterate through each element
    for i in range(n):
        for j in range(n):
            #if not diagonal element
            if i != j:
                #set some random edges to max
                if random.random() < edge_probability:
                    #set most edges to weights between 1 and 100
                    matrix[i][j] = random.randint(1, 100)
                else:
                    matrix[i][j] = maxVal
    return matrix

def main():
    #different values of n, representing number of vertices, to test on
    ns = [10, 100, 1000, 10000, 100000, 1000000, 10000000]
    #for each value of n
    for n in ns:
        #create nxn array  
        matrix = generate_graph(n)
        #take time program starts at
        start = time.time()
        graph_diameter(matrix.copy())
        #calculate the amount of time program took to run for input n 
        print(f"program with n = {n} took {time.time() - start} seconds")

if __name__ == "__main__":
    main()