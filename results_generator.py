import math
import os

from pylatex import Document, Section, Tabular, MultiColumn

from costs_generator import generate_costs
from sweep import sweep
from nearest_insertion import nearest_insertion
from farthest_insertion import farthest_insertion
from kNN import kNN, opt_kNN

# Embedded algorithm names
supported_algorithms = ['sweep', 'knn', 'knn-opt', 'nearest_insertion', 'farthest_insertion']
algorithm_name_dict = {
    'sweep': 'Sweep',
    'knn': 'Nearest Neighbour',
    'knn-opt': 'Nearest Neighbour Optimized',
    'nearest_insertion': 'Nearest Insertion',
    'farthest_insertion': 'Farthest Insertion'
}

# Embedded wind directions
north = math.pi/2
south = (math.pi/2)*3
east = 0
west = math.pi
winds = [north, south, east, west]

# Embedded topology maps
map1 = [(8,6), (4,8), (13,3), (10,5), (8,4), (7,3), (5,4), (4,6), (7,7), (8,8), (10,8), (13,10), (12,5), (3,3), (9,2)]
map2 = [(18,4), (1,2), (3,4), (0,2), (8,14), (7,13), (5,5), (4,7), (3,7), (10,11), (15,3), (3,0), (2,5), (13,14), (9,7)]
map3 = [(20,1), (14,4), (1,3), (4,2), (8,3), (2,10), (12,1), (9,10), (2,8), (7,1), (7,5), (9,5), (16,8), (5,8), (7,7)]
map4 = [(11,2), (3,9), (12,4), (1,3), (6,4), (4,7), (1,3), (4,2), (8,3), (13,10), (12,5), (3,3), (12,1), (9,10), (0,0)]
maps = [map1, map2, map3, map4]

# Best solutions
real_optimum = [39.49, 39.49, 39.49, 39.49,
                58.91, 58.91, 58.91, 58.91,
                60.02, 60.02, 60.02, 60.02,
                44.81, 44.81, 44.81, 44.81]


def generate_table_all_16(algorithm):

    # If the algorithm is not supported we do not create anything
    if algorithm not in supported_algorithms:
        print("We cannot generate the table!")
    else:
        # Creating the document
        doc = Document('latex_tables/generated_table_all_16_' + algorithm)
        section = Section(algorithm_name_dict[algorithm] + " Table")

        # Creation of the Table
        table = Tabular('ccc')
        table.add_row((MultiColumn(3, align='c', data=algorithm_name_dict[algorithm]),))
        table.add_hline()
        table.add_hline()
        table.add_row(("ID", "Soluzione", "Tempo"))
        table.add_hline()

        # Iterating for each map with respect to the wind
        map_index = 1
        for current_map in maps:
            for current_wind in winds:
                tot_cost = 0
                tot_time = 0

                # We catch the correct algorithm to use
                if algorithm == 'sweep':
                    tot_cost, tot_time, path = sweep(current_map, generate_costs(current_map, current_wind), plot=False)

                if algorithm == 'knn':
                    tot_cost, tot_time, path = kNN(generate_costs(current_map, current_wind), 0)

                if algorithm == 'knn-opt':
                    tot_cost, tot_time, path = opt_kNN(generate_costs(current_map, current_wind))

                if algorithm == 'nearest_insertion':
                    tot_cost, tot_time, path = nearest_insertion(generate_costs(current_map, current_wind))

                if algorithm == 'farthest_insertion':
                    tot_cost, tot_time, path = farthest_insertion(generate_costs(current_map, current_wind))

                # The row with the data is written onto a new row and the index is incremented
                table.add_row((map_index, "{:.2f}".format(tot_cost), "{:.2e}".format(tot_time)))
                map_index += 1

        # We close the table
        table.add_hline()

        # And finally we compose and generate the new document with the embedded table
        section.append(table)
        doc.append(section)
        doc.generate_tex()


def generate_comparison(dims, algorithm_names, algorithm_results, mode='COST'):

    # Creating the document
    from_mode = ''
    if mode == 'COST':
        doc = Document('latex_tables/generated_table_cost_comparison')
        section = Section("Table of Costs")
        from_mode = "{:.2f}"
    if mode == 'TIME':
        doc = Document('latex_tables/generated_table_time_comparison')
        section = Section("Table of Times")
        from_mode = "{:.2e}"

    # Setting tabular property
    tabular_header = 'c'
    for i in algorithm_names:
        tabular_header += 'c'

    # Creation of the Table
    table = Tabular(tabular_header)
    table.add_row((MultiColumn(len(algorithm_names)+1, align='c', data='Costs'),))
    table.add_hline()
    table.add_hline()
    table.add_row(['Nodi'] + algorithm_names)
    table.add_hline()

    for i in range(len(dims)):

        table.add_row((dims[i],
                       from_mode.format(algorithm_results[0][i]),
                       from_mode.format(algorithm_results[1][i]),
                       from_mode.format(algorithm_results[2][i]),
                       from_mode.format(algorithm_results[3][i]),
                       from_mode.format(algorithm_results[4][i])))

    # We close the table
    table.add_hline()

    # And finally we compose and generate the new document with the embedded table
    section.append(table)
    doc.append(section)
    doc.generate_tex()


# Generate loss percentage
# Creating the document
def generate_loss_wrt_optimum():

    # Creating the document
    from_mode = ''
    doc = Document('latex_tables/generated_loss_wrt_optimum')
    section = Section("Table of Costs")
    from_mode = "{:.2f}"

    # Setting tabular property
    tabular_header = 'cccccc'

    # Creation of the Table
    table = Tabular(tabular_header)
    table.add_row((MultiColumn(6, align='c', data='Costs'),))
    table.add_hline()
    table.add_hline()
    table.add_row(['ID'] + supported_algorithms)
    table.add_hline()

    # Iterating for each map with respect to the wind
    map_index = 1

    for current_map in maps:
        for current_wind in winds:

            # We catch the correct algorithm to use
            tot_cost_0, _, _ = sweep(current_map, generate_costs(current_map, current_wind), plot=False)
            tot_cost_1, _, _ = kNN(generate_costs(current_map, current_wind), 0)
            tot_cost_2, _, _ = opt_kNN(generate_costs(current_map, current_wind))
            tot_cost_3, _, _ = nearest_insertion(generate_costs(current_map, current_wind))
            tot_cost_4, _, _ = farthest_insertion(generate_costs(current_map, current_wind))

            # The row with the data is written onto a new row and the index is incremented
            print(map_index)
            table.add_row((map_index,
                           "{:.2f}".format(((tot_cost_0/real_optimum[map_index-1])-1)*100) + '%',
                           "{:.2f}".format(((tot_cost_1/real_optimum[map_index-1])-1)*100) + '%',
                           "{:.2f}".format(((tot_cost_2/real_optimum[map_index-1])-1)*100) + '%',
                           "{:.2f}".format(((tot_cost_3/real_optimum[map_index-1])-1)*100) + '%',
                           "{:.2f}".format(((tot_cost_4/real_optimum[map_index-1])-1)*100) + '%'))

            map_index += 1

    # We close the table
    table.add_hline()

    # And finally we compose and generate the new document with the embedded table
    section.append(table)
    doc.append(section)
    doc.generate_tex()

generate_table_all_16('sweep')
generate_table_all_16('knn')
generate_table_all_16('knn-opt')
generate_table_all_16('nearest_insertion')
generate_table_all_16('farthest_insertion')
generate_loss_wrt_optimum()
