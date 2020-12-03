import math
import sys
import random
import time
import numpy as np
from copy import copy, deepcopy


def farthest_insertion(G, starting_node = 0):
    if type(G) == np.ndarray:
        G = G.tolist()

    inf = sys.float_info.max
    N = len(G[0])
    M = deepcopy(G)
    C = []  # Cycle C (initialized to empty set)

    for i in range(N):
        M[i][i] = -inf
        G[i][i] = inf

    t0 = time.time()  # Starting the timer

    C.append(starting_node)
    C.append(M[starting_node].index(max(M[starting_node])))

    while len(C) < len(G):
        #i = random.choice(range(len(C)))
        max_found = False

        # Find the the node with maximum cost to any node of C and add it to the cycle
        while(max_found == False):
            max_value = max(M[i])

            if (max_value == -inf):
                i = (i+1)%(len(C))

            j = M[i].index(max_value)  # Finds the node j such that arc (i, j) with maximum cost (for all arcs steaming from i)

            if ((j in C) == False):
                new_node = j
                max_found = True
            else:
                M[i][j] = -inf

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
G = [[inf, 6.12, 11.1, 4.33, 3.83],
    [2.12, inf, 8.56, 5.72, 2.61],
    [6.1, 7.56, inf, 4.25, 4.33],
    [7.33, 12.72, 12.25, inf, 8.33],
    [1.83, 4.61, 7.33, 3.33, inf]]

output, tot_time = farthest_insertion(G)
print(output)

final_cost = 0
for i in range(len(output)):
    final_cost = final_cost + G[output[i]][(output[(i+1)%len(output)])]
    print("(" + str(output[i]) + ", " + str(output[(i+1)%len(output)]) + "): " + str(G[output[i]][(output[(i+1)%len(output)])]))

print("Final cost: " + str(final_cost))
'''
