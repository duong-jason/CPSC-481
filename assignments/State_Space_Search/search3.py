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
START, FINAL = [1, 4, 3, 7, 0, 6, 5, 8, 2], [1, 2, 3, 4, 5, 6, 7, 8, 0]

ACTION = (
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

        if curr.state != FINAL:
            for move in ACTION[curr.blank]:
                child = curr.state.copy()

                child[curr.blank], child[move] = child[move], child[curr.blank]

                if child not in CLOSED:
                    node = State(move, curr.state, child, move)
                    #node = State(move, front, child,
                    #            DIR[(blank, move)])
                    curr.next = node
                    return self.dfs(node)

        return None

    def bfs(self):
        """breadth-first search implementation"""
        OPEN = [self]
        CLOSED.append(self.state)

        while OPEN:
            front, blank = OPEN[0].state, OPEN[0].blank
            for move in ACTION[blank]:
                child = front.copy()

                child[blank], child[move] = child[move], child[blank]

                if child not in CLOSED:
                    CLOSED.append(child)
                    node = State(move, front, child, move)
                    #node = State(move, front, child,
                    #            DIR[(blank, move)])
                    OPEN.append(node)
                    #print("State: {} Move: {}".format(front, DIR[(blank, move)]))
                    print("State: {} Move: {}".format(front, move))

            if front == FINAL:
                break

            OPEN.pop(0)

        print("Number of Visited Nodes:", len(CLOSED))


if __name__ == "__main__":
    """
    print("DFS")
    T1 = State(BLANK, None, START, None)
    T1.dfs(T1)
    T1.get_moves(T1)

    CLOSED = []
    """

    print("\nBFS")
    T2 = State(BLANK, None, START, None)
    T2.bfs()
