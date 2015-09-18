
# The A* algorithm is for shortest path from start to goal in a grid maze
# The algorithm has many different choices:
# choose large or small g when f values are equal; forward or backward; adaptive or not


from GridWorlds import create_maze_dfs, set_state, get_grid_size, draw_grid
from classes import Heap, State
import Tkinter

# ------------------------------ initialization ------------------------------ #

# create original grid of state of size (col, row)
def create_state(col=100, row=100):


# ------------------------------- start A* ------------------------------------ #

# global movement [[0, 0, up, down], [left, right, 0, 0]]
move = [[0, 0, -1, 1], [-1, 1, 0, 0]]


# action is int from 0 to 3, represents left, right, up, down; position is (c, r); state is the state grid
def get_succ(states, position, action):


# if action is available, cost is 1, otherwise cost is 0
def cost(state, position, action):


# --------------------------------------------- #
# search for a new path when original one blocked
def compute_path(states, goal, open_list, close_list, counter, expanded, large_g, adaptive):


# --------------------------------------- A* search ---------------------------------------- #
# (path, exist) = A_star_forward(start, goal, maze_grid, large_g="large", forward="forward", adaptive="adaptive"
#
#  input: start, goal: the coordinates (x, y) of start and goal
#         maze_grid:   a grid maze created by create_maze_dfs() function in GridWorlds
#         large_g:     "large" to choose large g when f are same, otherwise choose small g
#         forward:     "forward" to choose forward A*, otherwise choose backward A*
#         adaptive:    "adaptive" to choose adaptive A*, otherwise choose A*
#
# output: path:  array of coordinates (x, y) of path nodes from start to goal
#         exist: boolean, "True" if path exists, "False" otherwise

def A_star_forward(start, goal, maze_grid, large_g="large", adaptive="adaptive"):


# draw the path from start to goal
def draw_path(maze_grid, path):

