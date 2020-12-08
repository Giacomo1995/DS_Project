import matplotlib.pyplot as plt


# Function used for visualize the map topology
def visualize_map(topology):

    xs, ys = __get_coords(topology)

    plt.scatter(xs, ys)
    plt.show()


# Function used for visualize a topology with his path
def visualize_path(path, topology):

    xs, ys = __get_coords(topology)

    for i in range(len(path)):

        if i == len(path)-1:
            p1 = topology[path[i]]
            p2 = topology[path[0]]
        else:
            p1 = topology[path[i]]
            p2 = topology[path[i+1]]

        val1 = [p1[0], p2[0]]
        val2 = [p1[1], p2[1]]
        plt.plot(val1, val2, 'y')

    plt.scatter(xs, ys)
    plt.show()


def plot_comparison(resut_list):

    for element in resut_list:
        plt.plot(element)

    plt.show()


def __get_coords(topology):

    xs = []
    ys = []

    # We get the list of xs and ys
    for i in range(len(topology)):
        xs.append(topology[i][0])
        ys.append(topology[i][1])

    return xs, ys

