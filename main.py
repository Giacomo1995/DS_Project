from costs_generator import generate_costs
from farthest_insertion import farthest_insertion
from map_generator import generate_map
from nearest_insertion import nearest_insertion
from results_generator import generate_comparison
from sweep import sweep
from kNN import kNN, opt_kNN

dims = [10, 25, 50, 100, 200, 500, 1000]
n_means = 10
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

    sweep_curr_cost = 0
    sweep_curr_time = 0
    nearest_neighbour_curr_cost = 0
    nearest_neighbour_curr_time = 0
    nearest_neighbour_opt_curr_cost = 0
    nearest_neighbour_opt_curr_time = 0
    nearest_insertion_curr_cost = 0
    nearest_insertion_curr_time = 0
    farthest_insertion_curr_cost = 0
    farthest_insertion_curr_time = 0

    for i in range(n_means):

        print(" = Generating maps for " + str(dim) + " nodes =")
        current_map = generate_map(dim)

        # Uptating Sweep
        print("Generating sweep...")
        c, t, _ = sweep(current_map, generate_costs(current_map, 0), plot=False)
        sweep_curr_cost += c
        sweep_curr_time += t
        print("Sweep time: " + "{:.2f}".format(t))

        # Uptating Nearest Neighbour
        print("Generating nearest neighbour...")
        c, t, _ = kNN(generate_costs(current_map, 0), 0)
        nearest_neighbour_curr_cost += c
        nearest_neighbour_curr_time += t
        print("Nearest neighbour time: " + "{:.2f}".format(t))


        # Uptating Optimized Nearest Neighbour
        print("Generating optimized nearest neighbour...")
        c, t, _ = opt_kNN(generate_costs(current_map, 0))
        nearest_neighbour_opt_curr_cost += c
        nearest_neighbour_opt_curr_time += t
        print("Optimized nearest neighbour time: " + "{:.2f}".format(t))

        # Uptating Nearest Insertion
        print("Generating nearest insertion...")
        c, t, _ = nearest_insertion(generate_costs(current_map, 0))
        nearest_insertion_curr_cost += c
        nearest_insertion_curr_time += t
        print("Nearest insertion time: " + "{:.2f}".format(t))

        # Uptating Farthest Insertion
        print("Generating farthest insertion...")
        c, t, _ = farthest_insertion(generate_costs(current_map, 0))
        farthest_insertion_curr_cost += c
        farthest_insertion_curr_time += t
        print("Farthest insertion time: " + "{:.2f}".format(t))

    sweep_costs.append(sweep_curr_cost/n_means)
    sweep_times.append(sweep_curr_time/n_means)
    nearest_neighbour_costs.append(nearest_neighbour_curr_cost/n_means)
    nearest_neighbour_times.append(nearest_neighbour_curr_time/n_means)
    nearest_neighbour_opt_costs.append(nearest_neighbour_opt_curr_cost/n_means)
    nearest_neighbour_opt_times.append(nearest_neighbour_opt_curr_time/n_means)
    nearest_insertion_costs.append(nearest_insertion_curr_cost/n_means)
    nearest_insertion_times.append(nearest_insertion_curr_time/n_means)
    farthest_insertion_costs.append(farthest_insertion_curr_cost/n_means)
    farthest_insertion_times.append(farthest_insertion_curr_time/n_means)

    
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

