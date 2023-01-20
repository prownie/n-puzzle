import math
#Distance for each tile to goal placement

def manhattanDistance(grid, goal, size, memo={}):
    # Vérification de la présence du coût de Manhattan de la grille dans le dictionnaire de mémoïsation
    if grid in memo:
        return memo[grid]
    
    # Préparation des positions cibles pour chaque case
    goal_pos = [0] * (size*size)
    for i in range(size*size):
        goal_pos[goal[i]] = i
    
    # Calcul du coût de Manhattan
    cost = 0
    for index in range(size * size):
        if (grid[index] == 0):
            continue
        
        # Calcul des positions actuelles et cibles de la case
        row = index % size
        col = index // size
        goal_row, goal_col = goal_pos[grid[index]] % size, goal_pos[grid[index]] // size
        
        # Ajout de la distance de Manhattan à la case à la somme totale
        cost += abs(goal_row - row) + abs(goal_col - col)
    
    # Ajout du coût de Manhattan de la grille au dictionnaire de mémoïsation
    memo[grid] = cost
    
    return cost


	
def manhattanDistanceLinearConflict(grid, goal, size, memo={}):
    # Vérification de la présence du coût de Manhattan avec conflit linéaire de la grille dans le dictionnaire de mémoïsation
    if grid in memo:
        return memo[grid]
    
    # Préparation des positions cibles pour chaque case
    goal_pos = [0] * (size*size)
    for i in range(size*size):
        goal_pos[goal[i]] = i
    
    # Calcul du coût de Manhattan avec conflit linéaire
    cost = 0
    for index in range(size * size):
        if (grid[index] == 0):
            continue
        
        # Calcul des positions actuelles et cibles de la case
        row = index % size
        col = index // size
        goal_row, goal_col = goal_pos[grid[index]] % size, goal_pos[grid[index]] // size
        
        # Ajout de la distance de Manhattan à la case à la somme totale
        cost += abs(goal_row - row) + abs(goal_col - col)
        
        # Ajout de 1 si la case est en conflit linéaire
        if (goal_row == row and goal_col != col) or (goal_row != row and goal_col == col):
            cost += 1
    
    # Ajout du coût de Manhattan avec conflit linéaire de la grille au dictionnaire de mémoïsation
    memo[grid] = cost
    
    return cost


def misplacedTiles(grid, goal, size, memo={}):
    # Vérification de la présence du coût des tuiles mal placées de la grille dans le dictionnaire de mémoïsation
    if grid in memo:
        return memo[grid]

    # Calcul du coût des tuiles mal placées
    cost = sum(1 for i in range(size * size) if grid[i] != goal[i] and grid[i] != 0)

    # Ajout du coût des tuiles mal placées de la grille au dictionnaire de mémoïsation
    memo[grid] = cost

    return cost
