import random


def generate_map(num_nodes):

    # At the first time the fresh map is empty
    fresh_map = []

    # We add each node
    for i in range(num_nodes):

        # We generate a new point between 0 and num_nodes
        new_node = (random.randint(0, num_nodes), random.randint(0, num_nodes))

        # If there's a duplicate node we re-generate it
        while new_node in fresh_map:
            new_node = (random.randint(0, num_nodes), random.randint(0, num_nodes))

        # We add the new node
        fresh_map.append(new_node)

    return fresh_map

