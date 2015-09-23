

# -------------------------- class Heap --------------------------------- #

# binary heap for OPEN LIST in A*
class Heap(object):

    def __init__(self):

        # here every item in heap is array []
        # while the first element in array is a number used to build heap
        self.heap = []

    def renew_leaf(self, current):

        x = self.heap[current]

        # let x go up the heap
        while current > 0:
            parent = (current - 1) >> 1

            if x[0] < self.heap[parent][0]:
                # exchange x and its parent
                self.heap[current] = self.heap[parent]
                current = parent
                continue
            break
        self.heap[current] = x

    # insert an element into heap queen
    def insert(self, x):

        # add element x to the end
        self.heap.append(x)
        # move x to its correct position
        self.renew_leaf(len(self.heap)-1)

        return self

    # renew heap queen when root is removed
    def renew_root(self, position):

        # start from root
        current = position
        # left child of root
        child = position * 2 + 1


        while child < len(self.heap):
            right = child + 1

            # if right child is large than left, exchange them
            if right < len(self.heap) and self.heap[right][0] < self.heap[child][0]:
                child = right
            # move child up
            self.heap[current] = self.heap[child]

            # go to the position of the child that has been moved up
            current = child
            # get its left child
            child = current * 2 + 1

        left = current

        # return the empty leaf
        return left

    # pop the last element(the largest) in heap queen
    def pop(self):

        last = self.heap.pop()
        if len(self.heap) > 0:

            item = self.heap[0]
            # replace root with last element and renew the root
            self.heap[0] = last

            # get original root item
            root = self.heap[0]
            # renew the children of root
            left = self.renew_root(0)

            # fill the empty leaf with root
            self.heap[left] = root
            self.renew_leaf(left)

        # if only 1 element exists
        else:
            item = last

        return item

    # delete an element from heap
    def remove(self, position):

        # remove an element and renew its children
        leaf = self.renew_root(position)
        # fill the empty leaf with last leaf and renew
        last = self.heap.pop()

        # if left is not the last of original heap, renew that leaf
        if len(self.heap) > leaf:
            self.heap[leaf] = last
            self.renew_leaf(leaf)


# ---------------------------- class State ------------------------------- #

# class state
class State:

    # the five elements used for A*
    def __init__(self, position=(0, 0)):

        # the coordinate of the present
        self.position = position

        # 1 if visited, 0 otherwise
        self.visit = 0
        # f, g, h values for A*
        self.g = 10000
        self.h = 0
        self.f = self.h + self.g

        # tree, necessary to identify a shortest path after A* search
        self.tree = {}

        # search is x if the state is generated last by x_th A* search
        self.search = 0

        # actions contains movement left, right, up, down, 1 if available
        self.actions = [1, 1, 1, 1]

    # renew h and f
    def renew_hf(self, goal=(0,0)):

        # calculate Manhattan distance from current state to goal state
        dx = goal[0] - self.position[0]
        dy = goal[1] - self.position[1]
        self.h = abs(dx) + abs(dy)

        # renew self.f
        self.f = self.h + self.g

        # renew f
    def renew_f(self):

        # renew self.f
        self.f = self.h + self.g

    # calculate the cost of action
    def cost(self, action):

        # if unblocked
        if self.action_exist(action):
            c = 1
        else:
            c = 1000

        return c

    # check if action is available, return bool
    def action_exist(self, action):

        # if action is available, return true
        if self.actions[action] == 1:
            exist = True
        else:
            exist = False

        return exist

    # mark the action as unavailable
    def delete_action(self, action):

        # delete action by setting it 0
        self.actions[action] = 0
