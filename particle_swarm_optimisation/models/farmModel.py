import numpy as np

class Farm():
    def __init__(self, rows=10, cols=10) -> None:
        self.farm_area = np.random.randint(0, 2, size=(rows, cols))

    def divide_farm_area(self, grid_size):
        # Get the size of the farm area
        rows, cols = len(self.farm_area), len(self.farm_area[0])
        
        # Calculate the number of rows and columns for the grid
        num_rows = (rows + grid_size - 1) // grid_size
        num_cols = (cols + grid_size - 1) // grid_size
        
        # Create an empty grid
        grid = [[0 for _ in range(num_cols)] for _ in range(num_rows)]
        
        # Fill the grid with the values from the farm area
        for i in range(rows):
            for j in range(cols):
                if self.farm_area[i][j] != 0:
                    row = i // grid_size
                    col = j // grid_size
                    grid[row][col] = self.farm_area[i][j]
                    
        return grid
