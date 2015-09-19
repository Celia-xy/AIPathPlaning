
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


# get all neighbors of present cell
def get_neighbors((c, r), move):



# add elements in neighbors to dfs_list; neighbors(index) to be the last
def add_dfs(neighbors, open_list, index):



# get a unblocked cell
def get_unblocked(maze_grid):


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


# draw maze
def draw_grid(maze_grid):

