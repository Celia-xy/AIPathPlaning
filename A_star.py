
# The A* algorithm is for shortest path from start to goal in a grid maze
# The algorithm has many different choices:
# choose large or small g when f values are equal; forward or backward; adaptive or not


from GridWorlds import create_maze_dfs, set_state, get_grid_size, draw_grid
from classes import Heap, State
import Tkinter

# ------------------------------ initialization ------------------------------ #

# create original grid of state of size (col, row)
def create_state(col=100, row=100):

    # create grid
    state_grid = [[State() for i in range(col)] for i in range(row)]

    # change values in state
    for i in range(col):
        for j in range(row):

            # correct position
            state_grid[j][i].position = (i, j)

            # correct movement
            # if the first column, remove left
            if i == 0:
                state_grid[j][i].actions[0] = 0
            # if the first row, remove up
            if j == 0:
                state_grid[j][i].actions[2] = 0
            # if the last column, remove right
            if i == col-1:
                state_grid[j][i].actions[1] = 0
            # if the last row, remove down
            if j == col-1:
                state_grid[j][i].actions[3] = 0

    return state_grid


# ------------------------------- start A* ------------------------------------ #

# global movement [[0, 0, up, down], [left, right, 0, 0]]
move = [[0, 0, -1, 1], [-1, 1, 0, 0]]


# action is int from 0 to 3, represents left, right, up, down; position is (c, r); state is the state grid
def get_succ(states, position, action):

    # movement [[0, 0, up, down], [left, right, 0, 0]]
    global move

    (c, r) = position
    if states[r][c].action_exist(action):

        # get next position
        r_new = r + move[0][action]
        c_new = c + move[1][action]
        succ = states[r_new][c_new]

    return succ


# if action is available, cost is 1, otherwise cost is 0
def cost(state, position, action):

    # movement [[0, 0, up, down], [left, right, 0, 0]]
    global move

    (c, r) = position
    # if the action is available
    if state[r][c].action_exist(action):
        cost = 1
    else:
        cost = 1000

# --------------------------------------------- #
# search for a new path when original one blocked
def compute_path(states, goal, open_list, close_list, counter, expanded, large_g, adaptive):

    global move

    (cg, rg) = goal

    while states[rg][cg].g > open_list.heap[-1][1].f:

        # open_list is binary heap while each item contains two value: f, state
        # remove the smallest f value item from open_list heap
        last_item = open_list.pop()
        # add the state with smallest f value into close_list
        close_list.append(last_item[1])

        (c, r) = last_item[1].position

        for i in range(4):

            if states[r][c].action_exist(i):
                # get the successor of last item when action is i
                pos = (c, r)
                successor = get_succ(states, pos, i)

                # the position of successor
                r_succ = r + move[0][i]
                c_succ = c + move[1][i]

                try:
                    close_list.index((c_succ, r_succ))
                except ValueError:

                    if successor.search < counter:

                        # the successor state in state_grid
                        states[r_succ][c_succ].g = 10000
                        states[r_succ][c_succ].renew_hf(goal)
                        states[r_succ][c_succ].search = counter

                    if successor.g > states[r][c].g + states[r][c].cost(i):
                        states[r_succ][c_succ].g = states[r][c].g + states[r][c].cost(i)
                        states[r_succ][c_succ].renew_hf(goal)
                        states[r_succ][c_succ].tree = states[r][c]

                        succ_state = states[r_succ][c_succ]
                        # choose favor of large g or small g when f is equal
                        if large_g == "large":
                            succ_favor = states[r_succ][c_succ].f * 10000 - states[r_succ][c_succ].g
                        else:
                            succ_favor = states[r_succ][c_succ].f * 10000 + states[r_succ][c_succ].g

                        i = 0
                        while i < len(open_list.heap) and len(open_list.heap) > 0:

                            # if successor is in open list
                            if succ_state.position == open_list.heap[i][1].position:

                                # renew the g value in the corresponding open list item and renew heap
                                open_list.remove(i)

                            i += 1

                        # insert the successor into open list
                        open_list.insert([succ_favor, succ_state])
                        expanded += 1
                else:
                    continue

        if len(open_list.heap) == 0:
            break

    return states, open_list, close_list, expanded


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

    # initial state grid
    states = create_state(len(maze_grid), len(maze_grid[0]))

    # decide if goal is reached
    reach_goal = False

    counter = 0
    expanded = 0
    current = start
    (cg, rg) = goal
    path = []
    path2 = []

    # the current position
    while reach_goal == False:

        counter += 1
        (cs, rs) = current
        states[rs][cs].g = 0
        states[rs][cs].renew_hf(goal)
        states[rs][cs].search = counter
        states[rg][cg].g = 10000
        states[rg][cg].renew_hf(goal)
        states[rg][cg].search = counter

        # open_list is binary heap while each item contains two value: f, state
        open_list = Heap()
        # close_list only store state
        close_list = []

        open_state = states[rs][cs]
        # choose favor of large g or small g when f is equal
        if large_g == "large":
            open_favor = states[rs][cs].f * 1000 - states[rs][cs].g
        else:
            open_favor = states[rs][cs].f * 1000 + states[rs][cs].g

        # insert s_start into open list
        open_list.insert([open_favor, open_state])
        # compute path
        (states, open_list, close_list, expanded) = compute_path(states, goal, open_list, close_list, counter, expanded, large_g, adaptive)
        if len(open_list.heap) == 0:
            print "I cannot reach the target."
            break

        # get the path from goal to start by tree-pointer
        (cc, rc) = goal
        path = [(cc, rc)]

        while (cc, rc) != (cs, rs):
            (cc, rc) = states[rc][cc].tree.position
            path.append((cc, rc))

        # follow the path
        (c_0, r_0) = path[-1]

        while states[r_0][c_0].position != (cg, rg):

            # (c, r) = successor.position
            (c, r) = path.pop()

            try:
                index = path2.index((c, r))
            except ValueError:
                path2.append((c, r))
            else:
                for i in range(index+1, len(path2)):
                    path2.pop()

            try:
                index = path2.index((c, r))
            except ValueError:
                path2.append((c, r))
            else:
                for i in range(index+1, len(path2)):
                    path2.pop()
            if len(path2) > 4:
                (c1, r1) = path2[-4]
                (c2, r2) = path2[-1]
                if abs(c1-c2) + abs(r1-r2) == 1:
                    path2.pop(-3)
                    path2.pop(-2)

            # if blocked, stop and renew cost of all successors
            if maze_grid[r][c] == 1:
                states[r][c].g = 10000
                states[r][c].renew_hf(goal)

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

            (c_0, r_0) = (c, r)

        # set start to current position
        current = (c_0, r_0)

        if states[r_0][c_0].position == (cg, rg):
            reach_goal = True

    # if path from start to goal exists
    if reach_goal:

        # (cc, rc) = start
        # path = []
        #
        # while (cc, rc) != (cs, rs):
        #
        #     path.append((cc, rc))
        #     (cc, rc) = states[rc][cc].tree.position
        #
        # while len(path2) > 0:
        #     path.append(path2.pop())

        print "I reached the target"

        print path2

    return path2, reach_goal, expanded


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
