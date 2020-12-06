import math
import sys
import random
import time
import numpy as np
from copy import copy, deepcopy


def nearest_insertion(G, starting_node = 0):
    if type(G) == np.ndarray:
        G = G.tolist()

    inf = sys.float_info.max
    N = len(G[0])
    M = deepcopy(G)
    C = []  # Cycle C (initialized to empty set)

    for i in range(N):
        M[i][i] = inf
        G[i][i] = inf

    t0 = time.time()  # Starting the timer

    C.append(starting_node)
    C.append(G[starting_node].index(min(G[starting_node])))

    while len(C) < len(G):
        #i = random.choice(range(len(C)))
        min_found = False

        # Find the the node with minimum cost to any node of C and add it to the cycle
        while(min_found == False):
            min_value = min(M[i])
            if (min_value == inf):
                i = (i+1)%(len(C))

            j = M[i].index(min_value)  # Finds the node j such that arc (i, j) with minimum cost (for all arcs steaming from i)

            if ((j in C) == False):
                new_node = j
                min_found = True
            else:
                M[i][j] = inf

        # Find the arc to delete in order to insert the new node in cycle C
        min_cost = inf
        for k in range(len(C)):
            h = (k+1) % len(C)

            tmp = G[C[k]][new_node] + G[new_node][C[h]] - G[C[k]][C[h]]
            if (tmp < min_cost):
                min_cost = tmp
                arc = [k, h]

        if (arc[1] == 0):
            arc[1] = len(C)

        C = C[0:(arc[0]+1)] + [new_node] + C[arc[1]:]  # Updates cycle C

        if (len(C) == len(G[i])):
            final_cost = 0
            tot_time = time.time() - t0

            for i in range(len(C)):
                final_cost = final_cost + G[C[i]][(C[(i+1)%len(C)])]

            return final_cost, tot_time, C


# TEST

# Cost matrix
'''
inf = sys.float_info.max
G = [[0.,3.71,9.6,8.03,6.17,11.12,4.,8.71,10.31, 6.5,7.1,6.2,6.06,9.05,7.82], [9.71,0.,6.54,5.2,3.08,7.42,2.61,5.31,6.65,4.12,3.57, 2.6,5.47,5.35,4.12], [28.6,19.54,0.,4.66,10.5,7.57,16.68,14.63,5.6, 9.32,9.32,12.25,23.31,8.4,10.21], [24.03,15.2,1.66,0.,6.12,7.25,12.06,11.93,5.32, 4.66,5.74,8.33,19.42,6.58,7.33], [18.17,9.08,3.5,2.12,0.,6.22,6.47,7.57,4.81, 1.74,1.74,2.74,13.43,4.33,3.62], [29.12,19.42,6.57,9.25,12.22,0.,18.45,10.5,2., 12.8,9.57,12.1,21.14,5.11,8.33], [12.,4.61,5.68,4.06,2.47,8.45,0.,7.99,7.21, 2.5,3.9,3.5,10.06,6.4,5.31], [19.71,10.31,6.63,6.93,6.57,3.5,10.99,0.,3.78, 8.22,4.39,5.,10.78,2.47,2.61], [28.31,18.65,4.6,7.32,10.81,2.,17.21,10.78,0., 11.1,8.33,11.12,21.,4.5,7.6], [19.5,11.12,3.32,1.66,2.74,7.8,7.5,10.22,6.1, 0.,4.,5.47,15.9,6.28,6.], [20.1,10.57,3.32,2.74,2.74,4.57,8.9,6.39,3.33, 4.,0.,3.,13.99,2.61,2.], [17.2,7.6,4.25,3.33,1.74,5.1,6.5,5.,4.12, 3.47,1.,0.,11.12,3.,1.83], [10.06,3.47,8.31,7.42,5.43,7.14,6.06,3.78,7., 6.9,4.99,4.12,0.,5.5,4.56], [24.05,14.35,4.4,5.58,7.33,2.11,13.4,6.47,1.5, 8.28,4.61,7.,16.5,0.,3.24], [20.82,11.12,4.21,4.33,4.62,3.33,10.31,4.61,2.6, 6.,2.,3.83,13.56,1.24,0.]]
final_cost, tot_time = nearest_insertion(G)

print("Final cost: " + str(final_cost))
'''
