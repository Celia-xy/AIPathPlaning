
# Generate maze-like grid worlds of size 101*101 with depth-first search algorithm
# using random tie breaking.

import random
import Tkinter


# initial grid
grid = []


# get grid size as (col, row)
def get_grid_size(matrix):

    row = len(matrix)
    col = len(matrix[0])
    size = (col, row)

    return size


# get all unvisited cells in grid
def get_unvisited(matrix):

    (col, row) = get_grid_size(matrix)

    # for all unvisited cells
    unvisited_list = []

    # put all unvisited cells in unvisited_list
    for i in range(col):
        for j in range(row):
            if grid[j][i] == 0:
                unvisited_list.append((i, j))

    return unvisited_list


# with 70% probability mark a cell as unblocked
def mark_unblocked():

    check = random.randint(1, 100)
    if check <= 70:
        unblock = True
    else:
        unblock = False

    return unblock


# get all neighbors of present cell
def get_neighbors((c, r), move):

    global grid
    (col, row) = get_grid_size(grid)

    # for available neighbors
    neighbors = []

    # get all neighbors
    for i in range(len(move[0])):
        r_new = r + move[0][i]
        c_new = c + move[1][i]

        # if neighbor exist
        if r_new >= 0 and r_new < row and c_new >=0 and c_new < col:

            # if neighbor is unvisited
            if grid[r_new][c_new] == 0:
                # if unblocked
                if mark_unblocked():
                    # unblocked neighbor added
                    neighbors.append((c_new, r_new))
                else:
                    # mark it as visited
                    grid[r_new][c_new] = 1

    return neighbors


# add elements in neighbors to dfs_list; neighbors(index) to be the last
def add_dfs(neighbors, open_list, index):

    # if not empty
    if len(neighbors) > 0 and index >= 0 and len(neighbors) > index:

        # add all expanded_list elements in dfs_list
        for i in range(len(neighbors)):
            if i != index:
                open_list.append(neighbors[i])

        # expanded(index) is the last of dfs_list and will be expanded in next search
        open_list.append(neighbors[index])

    return open_list


# get a unblocked cell
def get_unblocked(maze_grid):

    # get size
    (col, row) = get_grid_size(maze_grid)

    # randomly get a unblocked cell
    get_next = True
    while get_next:
        c = random.randint(0, col - 1)
        r = random.randint(0, row - 1)

        # if unblocked
        if maze_grid[r][c] == 0:
            get_next = False

    cell_unblocked = (c, r)

    return cell_unblocked


# ----------------------------------- create maze ----------------------------------- #
# maze = create_maze_dfs(col, row): generate maze-like grid world of size 101*101
#  input: column, row
# output: maze_grid of size (col, row), 1 if maze_grid[row][col] blocked, 0 otherwise

def create_maze_dfs(col=101, row=101):

    # unvisited grid world
    global grid

    grid = [[0 for i in range(col)] for i in range(row)]

    # movement [[0, 0, up, down], [left, right, 0, 0]]
    move = [[0, 0, -1, 1], [-1, 1, 0, 0]]

    # for unblocked cells
    maze_grid = [[1 for i in range(col)] for i in range(row)]

    # DFS
    # open_list for DFS
    open_list = []

    # randomly select a start point
    r = random.randint(0, row-1)
    c = random.randint(0, col-1)
    cell = (c, r)

    open_list.append(cell)

    get_next = True
    while get_next:

        # start DFS
        (c, r) = open_list.pop()
        # mark (c, r) as unblocked in maze_grid
        maze_grid[r][c] = 0

        # if unvisited
        if grid[r][c] == 0:
            grid[r][c] = 1

            # get its neighbors and mark blocked cells
            neighbors = get_neighbors((c, r), move)

            # add neighbors to open_list
            if len(neighbors) > 0:
                # choose a neighbor randomly
                index = random.randint(0, len(neighbors)-1)
                # add all neighbors
                open_list = add_dfs(neighbors, open_list, index)

        if len(open_list) > 0:
            get_next = True

        # if open_list is empty
        else:
            unvisited_list = get_unvisited(grid)

            # if unvisited cells exist, use random tie breaking
            if len(unvisited_list) > 0:
                # randomly choose one for next search
                index = random.randint(0, len(unvisited_list)-1)
                open_list.append(unvisited_list[index])
                get_next = True

            # all the cells are visited
            else:
                get_next = False
    return maze_grid


#  set start and goal state
def set_state(maze_grid):

    # get a unblocked cell as start
    (c_1, r_1) = get_unblocked(maze_grid)
    start = (c_1, r_1)
    # set the cell in maze_grid as "A"
    maze_grid[r_1][c_1] = "A"

    # get another unblocked cell as goal
    (c_2, r_2) = get_unblocked(maze_grid)
    goal = (c_2, r_2)
    # set the cell in maze grid as "T"
    maze_grid[r_2][c_2] = "T"

    return start, goal, maze_grid


# draw maze
def draw_grid(maze_grid):

