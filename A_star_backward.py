
# A* algorithm is used for shortest path from start to goal in a grid maze
# The algorithm has many different choices:
# choose large or small g when f values are equal; forward or backward; adaptive or not


from GridWorlds import create_maze_dfs, set_state, get_grid_size
from classes import Heap, State
from A_star import compute_path, create_state, get_succ
import Tkinter


# --------------------------------------- A* search ---------------------------------------- #
# (path, exist) = A_star_backward(start, goal, maze_grid, large_g="large", adaptive="adaptive"
#
#  input: start, goal: the coordinates (x, y) of start and goal
#         maze_grid:   a grid maze created by create_maze_dfs() function in GridWorlds
#         large_g:     "large" to choose large g when f are same, otherwise choose small g
#         forward:     "forward" to choose forward A*, otherwise choose backward A*
#         adaptive:    "adaptive" to choose adaptive A*, otherwise choose A*
#
# output: path:  array of coordinates (x, y) of path nodes from start to goal
#         exist: boolean, "True" if path exists, "False" otherwise


def A_star_backward(start, goal, maze_grid, large_g="large", adaptive="normal"):



# draw the path from start to goal
def draw_path(maze_grid, path):



