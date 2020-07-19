import math
import numpy as np

# Wind directions
north = math.pi/2
south = (math.pi/2)*3
east = 0
west = math.pi

# Five island visual example
island_coordinates_5_example = [(7,7), (6,3), (14,2), (12,10), (9,5)]

# Final maps
map1 = [(8,6), (4,8), (13,3), (10,5), (8,4), (7,3), (5,4), (4,6), (7,7), (8,8), (10,8), (13,10), (12,5), (3,3), (9,2)]
map2 = [(18,4), (1,2), (3,4), (0,2), (8,14), (7,13), (5,5), (4,7), (3,7), (10,11), (15,3), (3,0), (2,5), (13,14), (9,7)]
map3 = [(20,1), (14,4), (1,3), (4,2), (8,3), (2,10), (12,1), (9,10), (2,8), (7,1), (7,5), (9,5), (16,8), (5,8), (7,7)]
map4 = [(11,2), (3,9), (12,4), (1,3), (6,4), (4,7), (1,3), (4,2), (8,3), (13,10), (12,5), (3,3), (12,1), (9,10), (0,0)]

def generate_costs(islands, wind_angle):

    # Support variables
    n_islands = len(islands)
    costs = np.zeros((n_islands, n_islands))

    # Iterating over raws and columns
    for i in range(n_islands):
        for j in range(n_islands):

            # We save the two island respectively to the cost matrix
            i1 = islands[i]
            i2 = islands[j]

            # We compute the x and y distance
            dx = (i2[0] - i1[0])
            dy = (i2[1] - i1[1])

            # We compute the distance and angle between the islands
            distance = math.sqrt(dx*dx + dy*dy)
            angle = math.atan2(dy, dx)

            # We update the cost matrix
            costs[i][j] = round(distance - (distance/2)*math.cos(angle-wind_angle), 2)

    return costs
