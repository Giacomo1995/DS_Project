import math
import sys
import random
import time
import numpy as np
from copy import copy, deepcopy


def kNN(G, starting_node = 0):
    if type(G) == np.ndarray:
        G = G.tolist()

    inf = sys.float_info.max
    N = len(G[0])
    M = deepcopy(G)
    C = []  # Path C initialized to empty set (only at the end it is going to be a cycle)

    for i in range(N):
        M[i][i] = inf
        G[i][i] = inf

    t0 = time.time()  # Starting the timer

    C.append(starting_node)
    i = starting_node

    while len(C) < len(G):
        min_found = False

        # Find the the node with minimum cost to any node of C and add it to the path
        while(min_found == False):
            min_value = min(M[i])
            j = M[i].index(min_value)  # Finds the node j such that arc (i, j) with minimum cost (for all arcs steaming from i)

            # Check whether the found node is already in the path C or not
            if ((j in C) == False):
                new_node = j
                min_found = True
            else:
                M[i][j] = inf

        C.append(new_node)  # Updates the path
        i = new_node  # Updates the index

        # All nodes have been found
        if (len(C) == len(G[i])):
            final_cost = 0
            tot_time = time.time() - t0

            for i in range(len(C)):
                final_cost = final_cost + G[C[i]][(C[(i+1)%len(C)])]

            return final_cost, tot_time, C


#  Optimize k-NN
def opt_kNN(G, starting_node=0):

    inf = sys.float_info.max
    min_cost = inf
    t0 = time.time()  # Starting the timer

    # Iterate the k-NN algorithm for all possible starting nodes and get the best solution (between the found ones)
    C = []
    for i in range(len(G[0])):
        final_cost, t, p = kNN(G, i)

        if (final_cost < min_cost):
            min_cost = final_cost
            C = p

    final_time = time.time() - t0
    return min_cost, final_time, C

# TEST

# Cost matrix
'''
inf = sys.float_info.max
G = [[0.,6.63,2.74,5.05,2.89,5.1,5.05,3.5,1.66,9.25,3.66, 4.06,1.91,7.25,5.68], [14.63,0.,14.8,5.32,7.33,2.74,5.32,7.57,10.31, 15.05,14.35,6.,16.54,9.08,7.99], [1.74,5.8,0.,5.55,3.,4.54,5.55,4.25,2.12,6.58,1., 4.56,3.,5.21,6.65], [15.05,7.32,16.55,0.,7.6,6.5,0.,4.66,10.5, 19.89,16.68,3.,16.68,14.63,2.66], [7.89,4.33,9.,2.6,0.,2.61,2.6,1.83,3.24, 12.72,9.08,1.66,9.71,8.21,4.21], [12.1,1.74,12.54,3.5,4.61,0.,3.5,5.,7.66, 13.99,12.25,3.62,14.,8.33,6.06], [15.05,7.32,16.55,0.,7.6,6.5,0.,4.66,10.5, 19.89,16.68,3.,16.68,14.63,2.66], [10.5,6.57,12.25,1.66,3.83,5.,1.66,0.,6.12, 16.54,12.54,0.91,12.06,11.93,2.47], [4.66,5.31,6.12,3.5,1.24,3.66,3.5,2.12,0., 11.1,6.47,2.5,6.47,7.57,4.54], [7.25,5.05,5.58,7.89,5.72,4.99,7.89,7.54,6.1,0.,4.6, 7.21,8.56,2.,9.9], [2.66,5.35,1.,5.68,3.08,4.25,5.68,4.54,2.47,5.6,0., 4.72,4.,4.33,7.], [12.06,6.,13.56,1.,4.66,4.62,1.,1.91,7.5, 17.21,13.72,0.,13.72,12.22,2.74], [0.91,7.54,3.,5.68,3.71,6.,5.68,4.06,2.47,9.56,4., 4.72,0.,7.99,6.04], [9.25,3.08,8.21,6.63,5.21,3.33,6.63,6.93,6.57, 6.,7.33,6.22,10.99,0.,8.95], [16.68,10.99,18.65,3.66,10.21,10.06,3.66,6.47,12.54, 22.9,19.,5.74,18.04,17.95,0.]]

final_cost, tot_time, C = kNN(G)
print("Final cost: " + str(final_cost))

final_cost, tot_time, C = opt_kNN(G)
print("Final cost opt: " + str(final_cost))
'''
