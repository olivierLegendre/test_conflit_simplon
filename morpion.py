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

def check_win(grid:dict)-> bool:
    if check_ligne(grid):
        return check_ligne(grid)
    if check_colonne(grid):
        return check_colonne(grid)
    if check_diago(grid):
        return check_diago(grid)
    return False

def check_ligne(grid):
    # Vérifier les lignes
    for ligne in grid:
        if grid[ligne][0]==grid[ligne][1] and grid[ligne][1]==grid[ligne][2]:
            if grid[ligne][0] == "_":
                return False
            else :
                return True, grid[ligne][0]

def check_colonne(grid):
    # Vérifier les colonnes
    for i in range(3):
        if grid["A"][i]==grid["B"][i] and grid["B"][i]==grid["C"][i]:
            if grid["A"][i] == "_":
                return False
            else :
                return True, grid["A"][i]

def check_diago(grid):
    if grid["A"][0] == grid["B"][1] and grid["B"][1]==grid["C"][2]:
        return True, grid["B"][1]
    if grid["A"][2] == grid["B"][1] and grid["B"][1]==grid["C"][0]:
        return True, grid["B"][1]
    return False


def main():
    my_grid = create_grid()
    my_grid["A"] = ["O", "", "_"]
    my_grid["B"] = ["X", "O", "_"]
    my_grid["C"] = ["X", "_", "O"]
    display_grid(my_grid)
    play_an_action(my_grid,'X',("A",1))
    print(f"is grid full ? {is_grid_full(my_grid)}")
    print(f"Vainqueur : {check_win(my_grid)}")

main()