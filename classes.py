

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

