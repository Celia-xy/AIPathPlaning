
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

    # initial state grid
    states = create_state(len(maze_grid), len(maze_grid[0]))

    # decide if goal is reached
    reach_goal = False
    path = [start]#
    counter = 0
    expanded = 0
    (cs, rs) = start
    (cg, rg) = goal
    # the current position
    while reach_goal == False:

        counter += 1

        states[rs][cs].g = 10000
        states[rs][cs].renew_hf((cs, rs))
        states[rs][cs].search = counter
        states[rg][cg].g = 0
        states[rg][cg].renew_hf((cs, rs))
        states[rg][cg].search = counter

        # open_list is binary heap while each item contains two value: f, state
        open_list = Heap()
        # close_list only store state
        close_list = []

        open_state = states[rg][cg]
        # choose favor of large g or small g when f is equal
        if large_g == "large":
            open_favor = states[rg][cg].f * 1000 - states[rg][cg].g
        else:
            open_favor = states[rg][cg].f * 1000 + states[rg][cg].g

        # insert s_goal into open list
        open_list.insert([open_favor, open_state])
        # compute path
        (states, open_list, close_list, expanded) = compute_path(states, (cs, rs), open_list, close_list, counter, expanded, large_g, adaptive)
        if len(open_list.heap) == 0:
            print "I cannot reach the target."
            break

        # get the path from start to goal by tree-pointer
        (c_0, r_0) = path[-1]

        while (c_0, r_0) != (cg, rg):

            (c, r) = states[r_0][c_0].tree.position

            # if blocked, stop and renew cost of all successors
            if maze_grid[r][c] == 1:
                states[r][c].g = 10000
                states[r][c].renew_hf((cs, rs))

                # set action cost
                if c - c_0 == 0:
                    # cannot move down
                    if r - r_0 == 1:
                        states[r_0][c_0].actions[3] = 0

                    # cannot move up
                    else:
                        states[r_0][c_0].actions[2] = 0
                else:
                    # cannot move right
                    if c - c_0 == 1:
                        states[r_0][c_0].actions[1] = 0

                    # cannot move left
                    else:
                        states[r_0][c_0].actions[0] = 0

                break

            else:
                path.append((c, r))
                (c_0, r_0) = (c, r)

        (cs, rs) = (c_0, r_0)

        # set start to current position
        if path[-1] == (cg, rg):
            reach_goal = True

    # if path from start to goal exists
    if reach_goal:

        print "I reached the target"
        print path

    return path, reach_goal, expanded


# draw the path from start to goal
def draw_path(maze_grid, path):

    # get size
    (col, row) = get_grid_size(maze_grid)

    screen = Tkinter.Tk()
    canvas = Tkinter.Canvas(screen, width=(col+2)*5, height=(row+2)*5)
    canvas.pack()

    # create initial grid world
    for c in range(1, col+2):
        canvas.create_line(c*5, 5, c*5, (row+1)*5, width=1)
    for r in range(1, row+2):
        canvas.create_line(5, r*5, (col+1)*5, r*5+1, width=1)

    # mark blocked grid as black, start state as red, goal as green
    for c in range(0, col):
        for r in range(0, row):

            # if blocked
            if maze_grid[r][c] == 1:
                canvas.create_rectangle((c+1)*5+1, (r+1)*5+1, (c+2)*5, (r+2)*5, fill="black")
            # if the path
            if (c, r) in path:
                # mark path as blue
                canvas.create_rectangle((c+1)*5+1, (r+1)*5+1, (c+2)*5, (r+2)*5, fill="blue")

            # if start
            if maze_grid[r][c] == "A":
                canvas.create_rectangle((c+1)*5+1, (r+1)*5+1, (c+2)*5, (r+2)*5, fill="red")
            # if goal
            if maze_grid[r][c] == "T":
                canvas.create_rectangle((c+1)*5+1, (r+1)*5+1, (c+2)*5, (r+2)*5, fill="green")

    screen.mainloop()


# test
my_maze = create_maze_dfs(101, 101)
(start, goal, my_maze) = set_state(my_maze)

# get path by A* search
(PATH, reach_goal, expanded) = A_star_backward(start, goal, my_maze, "large", "forward")

# if path exist, draw maze and path
if reach_goal:
    draw_path(my_maze, PATH)
    print expanded
else:
    print "Path doesn't exist"