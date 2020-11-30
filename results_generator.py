import math
import os

from pylatex import Document, Section, Subsection, Tabular, MultiColumn, MultiRow

from costs_generator import generate_costs
from sweep import sweep

# Embedded algorithm names
supported_algorithms = ['sweep', 'knn', 'knn-opt', 'near-ins', 'far-ins']
algorithm_name_dict = {
    'sweep': 'Sweep',
    'knn': 'Nearest Neighbour',
    'knn-opt': 'Nearest Neighbour Optimized',
    'near-ins': 'Nearest Insertion',
    'far-ins': 'Farthest Insertion'
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
                    tot_cost, tot_time = sweep(current_map, generate_costs(current_map, current_wind), plot=False)
                # TODO: catch the other algorithm - Nearest Neighbour, Nearest Insertion and Farthest Insertion

                # The row with the data is written onto a new row and the index is incremented
                table.add_row((map_index, "{:.2f}".format(tot_cost), "{:.2e}".format(tot_time)))
                map_index += 1

        # We close the table
        table.add_hline()

        # And finally we compose and generate the new document with the embedded table
        section.append(table)
        doc.append(section)
        doc.generate_pdf(clean_tex=False)


generate_table_all_16('sweep')





