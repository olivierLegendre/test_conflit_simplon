def create_grid() -> dict:
    """_summary_

    Returns:
       grid (dict)
    """
    grid = dict()
    grid["A"] =  ["_", "_", "_"]
    grid["B"] =  ["_", "_", "_"]
    grid["C"] =  ["_", "_", "_"]
    return grid

def display_grid(grid: dict):
    """Display the grid

    Args:
        grid (dict): The grid
    """
    for line in grid.values():
        print(line)

def is_valid_move():
    pass

def main():
    my_grid = create_grid()
    display_grid(my_grid)

main()