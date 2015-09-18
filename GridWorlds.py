
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

# ----------------------------------- create maze ----------------------------------- #
# maze = create_maze_dfs(col, row): generate maze-like grid world of size 101*101
#  input: column, row
# output: maze_grid of size (col, row), 1 if maze_grid[row][col] blocked, 0 otherwise

def create_maze_dfs(col=101, row=101):

# draw maze
def draw_grid(maze_grid):

