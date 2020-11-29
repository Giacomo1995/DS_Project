import math
import sys
import random
import time
import numpy as np
from copy import copy, deepcopy


def nearest_insertion(G, starting_node = 0):
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

    for i in range(N):
        #i = random.choice(range(len(C)))
        min_found = False

        # Find the the node with minimum cost to any node of C and add it to the cycle
        while(min_found == False):
            j = M[i].index(min(M[i]))  # Finds the node j such that arc (i, j) with minimum cost (for all arcs steaming from i)

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
            print("Time: " + str(time.time() - t0))
            return C


# TEST

# Cost matrix
inf = sys.float_info.max
G = [[0.,18.12,15.,19.11,9.14,9.71,12.54,12.82,13.8, 7.13,3.66,17.52,15.53,6.18,7.99], [16.12,0.,1.83,1.,7.89,7.03,3.5,3.33,2.89, 8.23,13.54,3.83,1.66,10.97,6.93], [15.,3.83,0.,4.61,6.18,5.35,1.74,1.66,1.5, 6.4,12.54,6.,0.91,9.14,5.21], [17.11,1.,2.61,0.,8.42,7.54,4.33,3.9,3.33, 8.95,14.53,4.61,2.11,11.69,7.8], [19.14,19.89,16.18,20.42,0.,1.91,13.99,11.56,12.1, 5.11,18.54,21.87,15.32,5.,10.57], [18.71,18.03,14.35,18.54,0.91,0.,12.25,9.71,10.21, 4.61,17.81,20.1,13.43,5.58,9.32], [13.54,6.5,2.74,7.33,4.99,4.25,0.,1.24,1.83, 4.81,11.2,7.89,3.,7.54,3.47], [15.82,8.33,4.66,8.9,4.56,3.71,3.24,0.,1., 5.21,13.7,10.57,3.83,7.9,5.], [16.8,7.89,4.5,8.33,5.1,4.21,3.83,1.,0., 6.06,14.65,10.5,3.24,8.71,6.], [14.13,17.23,13.4,17.95,2.11,2.61,10.81,9.21,10.06, 0.,13.43,18.54,13.,2.74,6.12], [2.66,14.54,11.54,15.53,7.54,7.81,9.2,9.7,10.65, 5.43,0.,13.87,12.15,5.68,5.21], [13.52,1.83,2.,2.61,7.87,7.1,2.89,3.57,3.5, 7.54,10.87,0.,2.6,10.2,5.72], [16.53,4.66,1.91,5.11,6.32,5.43,3.,1.83,1.24, 7.,14.15,7.6,0.,9.71,6.28], [16.18,22.97,19.14,23.69,5.,6.58,16.54,14.9,15.71, 5.74,16.68,24.2,18.71,0.,11.56], [10.99,11.93,8.21,12.8,3.57,3.32,5.47,5.,6., 2.12,9.21,12.72,8.28,4.56,0.]]
output = nearest_insertion(G)
print(output)

final_cost = 0
for i in range(len(output)):
    final_cost = final_cost + G[output[i]][(output[(i+1)%len(output)])]
    print("(" + str(output[i]) + ", " + str(output[(i+1)%len(output)]) + "): " + str(G[output[i]][(output[(i+1)%len(output)])]))

print("Final cost: " + str(final_cost))
