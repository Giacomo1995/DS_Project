from costs_generator import generate_costs
from farthest_insertion import farthest_insertion
from map_generator import generate_map
from nearest_insertion import nearest_insertion
from results_generator import generate_comparison
from sweep import sweep
from kNN import kNN, opt_kNN

dims = [10, 25, 50, 100, 200, 500, 1000]
sweep_costs = []
nearest_neighbour_costs = []
nearest_neighbour_opt_costs = []
nearest_insertion_costs = []
farthest_insertion_costs = []

sweep_times = []
nearest_neighbour_times = []
nearest_neighbour_opt_times = []
nearest_insertion_times = []
farthest_insertion_times = []

algorithm_names = ['Sweep', 'k-NN', 'Optimized k-NN', 'Nearest Insertion', 'Farthest Insertion']

for dim in dims:

    print(" = Generating maps for " + str(dim) + " nodes =")
    current_map = generate_map(dim)

    # Uptating Sweep
    print("Generating sweep...")
    c, t, _ = sweep(current_map, generate_costs(current_map, 0), plot=False)
    sweep_costs.append(c)
    sweep_times.append(t)
    print("Sweep time: " + "{:.2f}".format(t))

    # Uptating Nearest Neighbour
    print("Generating nearest neighbour...")
    c, t, _ = kNN(generate_costs(current_map, 0), 0)
    nearest_neighbour_costs.append(c)
    nearest_neighbour_times.append(t)
    print("Nearest neighbour time: " + "{:.2f}".format(t))

    nearest_neighbour_opt_costs.append(0)
    nearest_neighbour_opt_times.append(0) # TODO: remove this line and uncomment the below section
    # # Uptating Optimized Nearest Neighbour
    # print("Generating optimized nearest neighbour...")
    # c, t, _ = opt_kNN(generate_costs(current_map, 0))
    # nearest_neighbour_opt_costs.append(c)
    # nearest_neighbour_opt_times.append(t)
    # print("Optimized nearest neighbour time: " + "{:.2f}".format(t))

    # Uptating Nearest Insertion
    print("Generating nearest insertion...")
    c, t, _ = nearest_insertion(generate_costs(current_map, 0))
    nearest_insertion_costs.append(c)
    nearest_insertion_times.append(t)
    print("Nearest insertion time: " + "{:.2f}".format(t))

    # Uptating Farthest Insertion
    print("Generating farthest insertion...")
    c, t, _ = farthest_insertion(generate_costs(current_map, 0))
    farthest_insertion_costs.append(c)
    farthest_insertion_times.append(t)
    print("Farthest insertion time: " + "{:.2f}".format(t))

algorithm_costs = [sweep_costs,
                   nearest_neighbour_costs,
                   nearest_neighbour_opt_costs,
                   nearest_insertion_costs,
                   farthest_insertion_costs]

algorithm_times = [sweep_times,
                   nearest_neighbour_times,
                   nearest_neighbour_opt_times,
                   nearest_insertion_times,
                   farthest_insertion_times]

generate_comparison(dims, algorithm_names, algorithm_costs, 'COST')
generate_comparison(dims, algorithm_names, algorithm_times, 'TIME')

