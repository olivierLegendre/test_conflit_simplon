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

def is_valid_move(grid: dict, move: tuple) -> bool:
    if grid[tuple[0]][tuple[1]] == "_":
        return False
    else:
        return True

def main():
    my_grid = create_grid()
    display_grid(my_grid)

main()