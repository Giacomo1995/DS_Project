import time

import matplotlib.pyplot as plt
import math
from costs_generator import generate_costs


def sweep(topology, C, plot=True):

    # Starting the algorithm -> Starting the timer
    t0 = time.clock()

    # Support variables for baricenter and visualization
    xs = []
    ys = []
    sumx = 0
    sumy = 0

    for elem in topology:
        sumx += elem[0]
        sumy += elem[1]
        xs.append(elem[0])
        ys.append(elem[1])

    bar = (sumx/len(topology), sumy/len(topology))

    # Two separate paths for right and left points with respect to the baricenter
    polars_pos = []
    polars_neg = []

    # Obtaining the node angles
    for i in range(len(topology)):

        elem = topology[i]
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
    for i in range(len(polars)):
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
            p1 = topology[polars[i][1]]
            p2 = topology[polars[i+1][1]]
            val1 = [p1[0], p2[0]]
            val2 = [p1[1], p2[1]]
            plt.plot(val1, val2, 'y')

        plt.show()

    # Computes the total cost of the found path
    tot_cost = 0
    dim = len(P)
    for k in range(dim - 1):
        tot_cost += C[P[k]][P[(k + 1)]]
    tot_cost += C[P[dim - 1]][P[0]]

    total_time = t1-t0

    return tot_cost, total_time, P

