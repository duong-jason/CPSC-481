#!/usr/bin/env python3
# Jason Duong
# CPSC 481-01
# 2022-02-02
# reddkingdom@csu.fullerton.edu
# @duong-jason
#
# Assignment #1
#
"""3x3 tile puzzle implementation with DFS and BFS"""

BLANK = 4
START, GOAL = [1, 4, 3, 7, 0, 6, 5, 8, 2], [1, 2, 3, 4, 5, 6, 7, 8, 0]

TABLE = (
    (1, 3),
    (0, 2, 4),
    (1, 5),
    (0, 4, 6),
    (1, 3, 5, 7),
    (2, 4, 8),
    (3, 7),
    (4, 6, 8),
    (5, 7),
)

CLOSED = []


class State:
    """State Reprsentation"""

    def __init__(self, blank, state, parent=None, move=None):
        self.blank = blank
        self.state = state
        self.parent = parent
        self.next = None
        self.move = move

    def get_path(self, curr):
        """outputs the states and path needed to solve"""
        if curr is None:
            print("Number of Visited Nodes:", len(CLOSED))
            return None

        print("State: {} Move: {}".format(curr.state, curr.move))
        return self.get_path(curr.next)

    def dfs(self, top):
        """depth-first search implementation"""
        CLOSED.append(top.state)

        if top.state != GOAL:
            for move in TABLE[top.blank]:
                child = top.state.copy()
                child[top.blank], child[move] = child[move], child[top.blank]

                if child not in CLOSED:
                    top.next = State(move, child, top.state, move)
                    return self.dfs(top.next)

        return None

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
                    print("State: {} Move: {}".format(frontier.state, move))
                    print("Number of Visited Nodes:", len(CLOSED))
                    return None

                if child not in CLOSED:
                    print("State: {} Move: {}".format(frontier.state, move))
                    CLOSED.append(child)
                    OPEN.append(State(move, child, frontier.state, move))


if __name__ == "__main__":
    print("DFS")
    T1 = State(BLANK, START)
    T1.dfs(T1)
    T1.get_path(T1)

    CLOSED = []

    print("\nBFS")
    T2 = State(BLANK, START)
    T2.bfs()
