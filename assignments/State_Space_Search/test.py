#!/usr/bin/env python3
# Jason Duong
# CPSC 481-01
# 2022-02-02
# reddkingdom@csu.fullerton.edu
# @duong-jason
#
# Assignment #1
#
"""2x2 tile puzzle implementation with DFS and BFS"""

TABLE = ((1, 2), (0, 3), (3, 0), (2, 1))
ACTION = {
    (0, 1): "Right",
    (0, 2): "Down",
    (1, 0): "Left",
    (1, 3): "Down",
    (2, 3): "Right",
    (2, 0): "Up",
    (3, 2): "Left",
    (3, 1): "Up",
}

CLOSED = []

class Problem:
    def __init__(self, blank, start=None, goal=None):
        self.blank = blank
        self.start = start
        self.goal = goal

    def solve(self):
        path = State(self.blank, self.start)
        self.reconstruct(path.dfs(path))

    def reconstruct(self, node):
        """outputs the states and path needed to solve"""
        count = 0
        while node is not None:
            print("State: {} Move: {}".format(node.state, node.move))
            node = node.kid
            count += 1

        print("Number of Visited Nodes:", count)


problem = Problem(0, [0, 3, 2, 1], [1, 2, 3, 0])

GOAL = [1, 2, 3, 0]

class State(Problem):
    """State Reprsentation"""

    def __init__(self, blank, state, parent=None, move=None):
        self.blank = blank
        self.state = state
        self.parent = parent
        self.kid = None
        self.move = move

        Problem.__init__(self, blank, state)

    def dfs(self, top):
        """depth-first search implementation"""
        CLOSED.append(top.state)

        if top.state != GOAL:
            for move in TABLE[top.blank]:
                child = top.state.copy()
                child[top.blank], child[move] = child[move], child[top.blank]

                if child not in CLOSED:
                    top.kid = State(move, child, top.state, ACTION[(top.blank, move)])
                    return self.dfs(top.kid)

        return self

    def bfs(self):
        """breadth-first search implementation"""
        OPEN = [self] # queue data structure
        CLOSED.append(self.state) # closed list of visited states

        while OPEN:
            frontier = OPEN.pop(0)
            for move in TABLE[frontier.blank]:
                child = frontier.state.copy()
                child[frontier.blank], child[move] = child[move], child[frontier.blank]

                if frontier.state == GOAL:
                    print("State: {} Move: {}".format(frontier.state, ACTION[(frontier.blank, move)]))
                    print("Number of Visited Nodes:", len(CLOSED))
                    return None

                if child not in CLOSED:
                    print("State: {} Move: {}".format(frontier.state, ACTION[(frontier.blank, move)]))
                    CLOSED.append(child)
                    OPEN.append(State(move, child, frontier.state, ACTION[(frontier.blank, move)]))


if __name__ == "__main__":
    problem.solve()
