
from GridWorlds import create_maze_dfs, set_state, draw_grid
from A_star import A_star_forward, draw_path
from A_star_backward import A_star_backward

# 50 start points
starts = []
# 50 goals
goals = []
# 50 grid mazes (with starts and goals)
mazes = []

# create original maze of size 101*101 using DFS
my_maze = create_maze_dfs(101, 101)

# draw maze (should close the graph to continue)
draw_grid(my_maze)

# create 50 different starts and goals
for i in range(50):

    (starts[i], goals[i], mazes[i]) = set_state(my_maze)


# ----------------------------- large g ---------------------------------- #
# implement A* search in favor of large g when f values are same
lg_paths = []
lg_exist = []
lg_expanded = []

for i in range(50):

    # implement A*
    (lg_paths[i], lg_exist[i], lg_expanded[i]) = A_star_forward(starts[i], goals[i], mazes[i], "large", "regular")

# ----------------------------- small g ---------------------------------- #
# implement A* search in favor of small g when f values are same
sg_paths = []
sg_exist = []
sg_expanded = []

for i in range(50):

    # implement A*
    (sg_paths[i], sg_exist[i], sg_expanded[i]) = A_star_forward(starts[i], goals[i], mazes[i], "small", "regular")

# ----------------------------- backward ---------------------------------- #
# implement backward A* search
bk_paths = []
bk_exist = []
bk_expanded = []

for i in range(50):

    # implement A*
    (bk_paths[i], bk_exist[i], bk_expanded[i]) = A_star_backward(starts[i], goals[i], mazes[i], "large", "regular")

# ----------------------------- adaptive ---------------------------------- #
# implement adaptive A* search
adp_paths = []
adp_exist = []
adp_expanded = []

for i in range(50):

    # implement A*
    (adp_paths[i], adp_exist[i], adp_expanded[i]) = A_star_forward(starts[i], goals[i], mazes[i], "large", "adaptive")

# ---------------------------- show results ------------------------------- #

# choose any of the 50 grids (range: 0 to 49)
k = 10

# print and compare expanded nodes
print "The number of expanded nodes by A* (large g): " + lg_expanded[k]
print "The number of expanded nodes by A* (small g): " + sg_expanded[k]
print "The number of expanded nodes by A* (backward): " + bk_expanded[k]
print "The number of expanded nodes by A* (adaptive): " + adp_expanded[k]

# draw maze and path
# large g
if lg_exist[k]:
    draw_path(mazes, lg_paths[k])
else:
    print "Path doesn't exist"

# small g
if sg_exist[k]:
    draw_path(mazes, sg_paths[k])
else:
    print "Path doesn't exist"

# backward A*
if bk_exist[k]:
    draw_path(mazes, bk_paths[k])
else:
    print "Path doesn't exist"

# adaptive A*
if adp_exist[k]:
    draw_path(mazes, adp_paths[k])
else:
    print "Path doesn't exist"
