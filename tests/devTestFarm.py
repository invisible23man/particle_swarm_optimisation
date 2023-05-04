from particle_swarm_optimisation.models.farmModel import Farm
import pytest

@pytest.fixture
def farm():
    return Farm(rows=5, cols=6)

def test_divide_farm_area(farm):
    grid_size = 2
    
    # Divide the farm area into grids of size 2x2
    grid = farm.divide_farm_area(grid_size)
    
    # Check that the grid size is correct
    assert len(grid) == 3
    assert len(grid[0]) == 3
    
    # Check that the sum of each grid cell matches the corresponding area in the farm area
    assert grid[0][0] == farm.farm_area[:2, :2].sum()
    assert grid[0][1] == farm.farm_area[:2, 2:4].sum()
    assert grid[0][2] == farm.farm_area[:2, 4:].sum()
    assert grid[1][0] == farm.farm_area[2:4, :2].sum()
    assert grid[1][1] == farm.farm_area[2:4, 2:4].sum()
    assert grid[1][2] == farm.farm_area[2:4, 4:].sum()
    assert grid[2][0] == farm.farm_area[4:, :2].sum()
    assert grid[2][1] == farm.farm_area[4:, 2:4].sum()
    assert grid[2][2] == farm.farm_area[4:, 4:].sum()

