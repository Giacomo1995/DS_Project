import time

import matplotlib.pyplot as plt
import math
from costs_generator import generate_costs

# Wind directions
north = math.pi/2
south = (math.pi/2)*3
east = 0
west = math.pi

map1 = [(8,6), (4,8), (13,3), (10,5), (8,4), (7,3), (5,4), (4,6), (7,7), (8,8), (10,8), (13,10), (12,5), (3,3), (9,2)]
map2 = [(18,4), (1,2), (3,4), (0,2), (8,14), (7,13), (5,5), (4,7), (3,7), (10,11), (15,3), (3,0), (2,5), (13,14), (9,7)]
map3 = [(20,1), (14,4), (1,3), (4,2), (8,3), (2,10), (12,1), (9,10), (2,8), (7,1), (7,5), (9,5), (16,8), (5,8), (7,7)]
map4 = [(11,2), (3,9), (12,4), (1,3), (6,4), (4,7), (1,3), (4,2), (8,3), (13,10), (12,5), (3,3), (12,1), (9,10), (0,0)]


def sweep(map, C, plot=True):

    # Starting the algorithm -> Starting the timer
    t0 = time.clock()

    # Support variables for baricenter and visualization
    xs = []
    ys = []
    sumx = 0
    sumy = 0

    for elem in map:
        sumx += elem[0]
        sumy += elem[1]
        xs.append(elem[0])
        ys.append(elem[1])

    bar = (sumx/len(map), sumy/len(map))

    # Two separate paths for right and left points with respect to the baricenter
    polars_pos = []
    polars_neg = []

    # Obtaining the node angles
    for i in range(len(map)):

        elem = map[i]
        dx = elem[0] - bar[0]
        dy = elem[1] - bar[1]

        if dx != 0:
            theta = dy/dx
        else:
            theta = math.inf

        if dx <= 0:
            polars_neg.append((theta, i))
        else:
            polars_pos.append((theta, i))

    # Sorting by angle and merging the two lists
    polars_pos.sort()
    polars_neg.sort()
    polars = polars_pos + polars_neg

    # populating the list of visited nodes
    P = []
    for i in range(len(polars) - 1):
        P.append(polars[i][1])

    # Finished the algorithm -> Stopping the timer
    t1 = time.clock()

    # Starting the plotting routine
    if plot:

        # Plotting the baricenter
        plt.plot(xs, ys, '.')
        plt.plot(bar[0], bar[1], '.r')

        # Plotting the path
        for i in range(len(polars)-1):
            p1 = map[polars[i][1]]
            p2 = map[polars[i+1][1]]
            val1 = [p1[0], p2[0]]
            val2 = [p1[1], p2[1]]
            plt.plot(val1, val2, 'y')

        plt.show()

    # TODO: This fragment is repeated among each heuristic algorithm
    # Computes the total cost of the found path
    tot_cost = 0
    dim = len(P)
    for k in range(dim - 1):
        tot_cost += C[P[k]][P[(k + 1)]]
    tot_cost += C[P[dim - 1]][P[0]]

    total_time = t1-t0
    print('Cost: ' + str(tot_cost))  # Prints the total cost
    print('Time used: ' + "{:e}".format(total_time))

    return tot_cost, total_time


sweep(map4, generate_costs(map4, north), plot=False)


