import random
from particle_swarm_optimisation.models.farmModel import Farm

def assign_drone_positions(farm:Farm, n):
    # Get the dimensions of the farm area
    row_edges, col_edges  = farm.farm_area.shape[0], farm.farm_area.shape[1]
    grid = farm.farm_area

    # Initialize a list to hold the start and end positions for each drone
    drone_positions = []
        
    # Assign start and end positions for each drone
    for i in range(n):
        # Choose a random cell in the grid as the start position
        row, col = random.randint(0, row_edges-1), random.randint(0, col_edges-1)
        while grid[row][col] == 0:
            row, col = random.randint(0, row_edges-1), random.randint(0, col_edges-1)
        start_position = (row, col)
        
        # Choose a random cell in the grid as the end position
        row, col = random.randint(0, row_edges-1), random.randint(0, col_edges-1)
        while grid[row][col] == 0 and start_position != (row, col):
            row, col = random.randint(0, row_edges-1), random.randint(0, col_edges-1)
        end_position = (row, col)
        
        # Add the start and end positions to the list
        drone_positions.append((start_position, end_position))
    
    return drone_positions
