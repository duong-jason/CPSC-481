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

ACTION = ((1, 2), (0, 3), (3, 0), (2, 1))
DIR = {
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
PATH = []


class State:
    """State Reprsentation"""

    def __init__(self, blank, parent, state, move):
        self.blank = blank
        self.parent = parent
        self.state = state
        self.next = None
        self.move = move

    def get_moves(self, curr):
        """outputs the states and path needed to solve"""
        if curr is None:
            print("Number of Visited Nodes:", len(CLOSED))
            return None

        print("State: {} Move: {}".format(curr.state, curr.move))
        return self.get_moves(curr.next)

    def dfs(self, curr):
        """depth-first search implementation"""
        CLOSED.append(curr.state)

        if curr.state != GOAL:
            for move in ACTION[curr.blank]:
                child = curr.state.copy()

                child[curr.blank], child[move] = child[move], child[curr.blank]

                if child not in CLOSED:
                    curr.next = State(move, curr.state, child, DIR[(curr.blank, move)])
                    return self.dfs(curr.next)

        return None

    def bfs(self):
        """breadth-first search implementation"""
        OPEN = [(self, [self.state])]
        CLOSED.append(self.state)

        while OPEN:
            front, path = OPEN[0][0], OPEN[0][1]
            for move in ACTION[front.blank]:
                child = front.state.copy()

                child[front.blank], child[move] = child[move], child[front.blank]

                if front.state == GOAL:
                    return path
                elif child not in CLOSED:
                    CLOSED.append(child)
                    OPEN.append(
                        (
                            State(move, front.state, child, DIR[(front.blank, move)]),
                            path + [child],
                        )
                    )

            OPEN.pop(0)


if __name__ == "__main__":
    print("DFS")
    T1 = State(BLANK, None, START, None)
    T1.dfs(T1)
    T1.get_moves(T1)

    CLOSED = []

    print("\nBFS")
    T2 = State(BLANK, None, START, None)
    result = T2.bfs()
    print(result)
    print("Number of Visited Nodes:", len(result))
