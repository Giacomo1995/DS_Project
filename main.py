from costs_generator import generate_costs
from farthest_insertion import farthest_insertion
from map_generator import generate_map
from graphic_manager import visualize_map, visualize_path
from nearest_insertion import nearest_insertion
from sweep import sweep

new_map = generate_map(100)
visualize_map(new_map)

c, t, path1 = sweep(new_map, generate_costs(new_map, 0), plot=False)
print("Sweep: " + str(t) + " - Cost: " + str(c))
c, t, path2 = nearest_insertion(generate_costs(new_map, 0))
print("Nearest: " + str(t) + " - Cost: " + str(c))
c, t, path3 = farthest_insertion(generate_costs(new_map, 0))
print("Farthest: " + str(t) + " - Cost: " + str(c))

visualize_path(path1, new_map)
visualize_path(path2, new_map)
visualize_path(path3, new_map)

