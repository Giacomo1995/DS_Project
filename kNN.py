import math
import sys
from costs_generator import generate_costs
import time
# Cost matrix
inf = sys.float_info.max
prints_on = False

def kNN(C, start_node):

    # Starting the timer
    t0 = time.time()

    # Sets P of visited nodes (initially empty)
    P = []
    i = start_node
    num_nodes = len(C[0])

    # Fills the P set using the k-NN technique
    while True:
        if len(P) == num_nodes: # All nodes visited
            break

        min_cost = sys.float_info.max

        for j in range(num_nodes):
            if (i != j and (j not in P)):
                if (min_cost > C[i][j]):
                    min_cost = C[i][j] # Updates the min_cost value
                    v = j # v contains the current node that leads to minimum cost

            if j == (num_nodes-1):
                P.append(i) # Inserts the current node into the P set
                i = v # Updates i with the node with minimum cost

    # Computes the total cost of the found path
    tot_cost = 0
    dim = len(P)
    for k in range(dim-1):
        tot_cost += C[P[k]][P[(k+1)]]
    tot_cost += C[P[dim-1]][start_node]

    if prints_on:
        print('Cost: ' + str(tot_cost)) # Prints the total cost

    for i in range(len(P)):
        P[i] += 1

    tot_time = time.time() - t0
    if prints_on:
        print("Path: " + str(P)) # Prints the found path (the sequence of nodes)
        print("Time: " + str(tot_time))

    return tot_cost, tot_time, P


def opt_kNN(C):

    t0 = time.time()

    min_cost = inf
    min_P = []
    for i in range(len(C)):
        curr_cost, curr_time, curr_P = kNN(C, i)
        if curr_cost < min_cost:
            min_cost = curr_cost
            min_P = curr_P

    if prints_on:
        print(' --- --- --- --- ---')
        print('Optimistic knn result: ' + str(min))
        print('Time: ' + str(time.time()-t0))
        print(' --- --- --- --- ---')

    return min_cost, time.time()-t0, min_P


C = [[inf, 6.12, 11.1, 4.33, 3.83],
    [2.12, inf, 8.56, 5.72, 2.61],
    [6.1, 7.56, inf, 4.25, 4.33],
    [7.33, 12.72, 12.25, inf, 8.33],
    [1.83, 4.61, 7.33, 3.33, inf]]

c, t, p = kNN(C, 0)
print(c)
kNN(C, 0)
'''
print(' --- Mappa 1 --- NSEW')
kNN(generate_costs(map1, north), 0)
kNN(generate_costs(map1, south), 0)
kNN(generate_costs(map1, east), 0)
kNN(generate_costs(map1, west), 0)

print(' --- Mappa 2 --- NSEW')
kNN(generate_costs(map2, north), 0)
kNN(generate_costs(map2, south), 0)
kNN(generate_costs(map2, east), 0)
kNN(generate_costs(map2, west), 0)

print(' --- Mappa 3 --- NSEW')
kNN(generate_costs(map3, north), 0)
kNN(generate_costs(map3, south), 0)
kNN(generate_costs(map3, east), 0)
kNN(generate_costs(map3, west), 0)

print(' --- Mappa 4 --- NSEW')
kNN(generate_costs(map4, north), 0)
kNN(generate_costs(map4, south), 0)
kNN(generate_costs(map4, east), 0)
kNN(generate_costs(map4, west), 0)

print(' --- Mappa 5 --- NSEW')
kNN(generate_costs(map5, north), 0)
kNN(generate_costs(map5, south), 0)
kNN(generate_costs(map5, east), 0)
kNN(generate_costs(map5, west), 0)
'''
