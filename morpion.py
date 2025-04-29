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
    print()

def play_an_action(grid:dict, player:str, coord:tuple):
    """For the player 'X' or 'O', push the player symbol
    in the grid 'grid' at the coordinate 'coord'. coord[0]
    gives the line label, coord[1] gives the column number.

    Args:
        grid (dict): the grid
        player (str): the player symbol
        coord (tuple): the coordinate in the grid where to play

    Raises:
        ValueError: Only player 'X' and 'O' are allowed
    """

    if (player != 'X' and player != 'O'):
        raise ValueError("Only 'X' and 'O' player names are allowed.")
    else:
        if is_valid_move(grid, coord):
            grid[coord[0]][coord[1]] = player 
    display_grid(grid)

def is_valid_move(grid: dict, move: tuple) -> bool:
    """
    check if grid position is empty
    Args:
        grid (dict): _description_
        move (tuple): _description_

    Returns:
        bool: _description_
    """
    if grid[move[0]][move[1]] == "_":
            return False
    else:
        return True
    
def is_grid_full(grid:dict) -> bool:
    """
    check if grid is full
    Args:
        grid (dict): _description_

    Returns:
        bool: _description_
    """
    for line_name in grid.keys():
        for x in range(len(grid[line_name])):
            if grid[line_name][x]:
                return False
    return True

def main():
    my_grid = create_grid()
    display_grid(my_grid)
    play_an_action(my_grid,'X',("A",1))
    print(f"is grid full ? {is_grid_full(my_grid)}")


main()