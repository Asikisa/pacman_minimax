import math


class Node(object):
    def __init__(self, path_cost, state, parent, depth):
        # state = current state in that node
        self.pathCost = path_cost
        self.state = state
        self.parent = parent
        self.depth = depth
        self.heuristic = 0

    def set_heuristic(self, goal):
        self.heuristic = abs(self.state[0] - goal[0]) + abs(self.state[1] - goal[1])
        return self.heuristic
