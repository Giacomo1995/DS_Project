from map_generator import generate_map
from graphic_manager import visualize_map, visualize_path


new_map = generate_map(10)
visualize_map(new_map)
visualize_path([0,1,2,3,4,5,6,7,8,9], new_map)

