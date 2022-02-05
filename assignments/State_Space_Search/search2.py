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

BLANK = 0
START, GOAL = [0, 3, 2, 1], [1, 2, 3, 0]

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

f = open("output2.txt", "r+")
f.truncate(0)


class State:
    """State Reprsentation"""

    def __init__(self, blank, state, parent=None, move=None):
        self.blank = blank
        self.state = state
        self.parent = parent
        self.next = None
        self.move = move

    def get_moves(self, curr):
        """outputs the states and path needed to solve"""
        if curr is None:
            print("Number of Visited Nodes:", len(CLOSED), file=f)
            return None

        print("State: {} Move: {}".format(curr.state, curr.move), file=f)
        return self.get_moves(curr.next)

    def dfs(self, top):
        """depth-first search implementation"""
        CLOSED.append(top.state)

        if top.state != GOAL:
            for move in TABLE[top.blank]:
                child = top.state.copy()
                child[top.blank], child[move] = child[move], child[top.blank]

                if child not in CLOSED:
                    top.next = State(move, child, top.state, ACTION[(top.blank, move)])
                    return self.dfs(top.next)

        return None

    def bfs(self):
        """breadth-first search implementation"""
        OPEN = [self]
        CLOSED.append(self.state)

        while OPEN:
            front = OPEN[0]
            for move in TABLE[front.blank]:
                child = front.state.copy()

                child[front.blank], child[move] = child[move], child[front.blank]

                if front.state == GOAL:
                    print("State: {} Move: {}".format(front.state, ACTION[(front.blank, move)]), file=f)
                    print("Number of Visited Nodes:", len(CLOSED), file=f)
                    return None

                if child not in CLOSED:
                    print("State: {} Move: {}".format(front.state, ACTION[(front.blank, move)]), file=f)
                    CLOSED.append(child)
                    OPEN.append(State(move, child, front.state, ACTION[(front.blank, move)]))

            OPEN.pop(0)


if __name__ == "__main__":
    print("DFS", file=f)
    T1 = State(BLANK, START)
    T1.dfs(T1)
    T1.get_moves(T1)

    CLOSED = []

    print("\nBFS", file=f)
    T2 = State(BLANK, START)
    T2.bfs()

    f.close()
