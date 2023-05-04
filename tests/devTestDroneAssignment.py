from particle_swarm_optimisation.models.droneModel import assign_drone_positions
from particle_swarm_optimisation.models.farmModel import Farm
import pytest

@pytest.fixture
def farm():
    # Create a farm area
    return Farm(rows=10, cols=10)

def test_assign_drone_positions(farm:Farm):    
    # Retrive Farm Parameters
    grid, grid_rows, grid_cols = farm.farm_area, farm.farm_area.shape[0], farm.farm_area.shape[1]

    # Assign drone positions
    n_drones = 3
    drone_positions = assign_drone_positions(farm, n_drones)
    print(grid, drone_positions)
    
    # Check that the number of drone positions match the number of drones
    assert len(drone_positions) == n_drones
    
    # Check that start and end positions are within the farm area and not on grids that should not be visited
    for i in range(n_drones):
        start_row, start_col = drone_positions[i][0]
        end_row, end_col = drone_positions[i][1]
        assert (start_row >= 0 and start_row < grid_rows) == True
        assert (start_col >= 0 and start_col < grid_cols) == True
        assert (end_row >= 0 and end_row < grid_rows) == True
        assert (end_col >= 0 and end_col < grid_cols) == True
        assert (grid[start_row][start_col]) == True
        assert (grid[end_row][end_col]) == True
