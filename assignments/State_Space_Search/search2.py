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
START, FINAL = [0, 3, 2, 1], [1, 2, 3, 0]

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

PATH = []
MOVE = [None]


class State:
    def __init__(self, blank, parent, state, move):
        self.blank = blank
        self.parent = parent
        self.state = state
        self.next = None
        self.move = move

    def getMoves(self, curr):
        while curr != None:
            print("{} | {} -> ".format(curr.move, curr.state), end='')
            curr = curr.next
        print("goal")

    def dfs(self, curr):
        """depth-first search implementation"""
        PATH.append(curr.state)

        if curr.state != FINAL:
            for move in ACTION[curr.blank]:
                child = curr.state.copy()

                child[curr.blank], child[move] = child[move], child[curr.blank]

#                print(curr.state, " -> ", child)
                if child not in PATH:
                    node = State(move,
                                 curr.state,
                                 child,
                                 DIR[(curr.blank, move)])
                    curr.next = node # next pointer
                    return self.dfs(node)

        return None


def dfs(state, blank):
    """depth-first search implementation"""
    PATH.append(state)

    if state != FINAL:
        for move in ACTION[blank]:
            child = state.copy()
            child[blank], child[move] = child[move], child[blank]

            if child not in PATH:
                MOVE.append(DIR[(blank, move)])
                return dfs(child, move)

    return None


def bfs():
    """breadth-first search implementation"""
    queue, symbol = [START], [BLANK]
    PATH.append(START)

    while queue:
        front, blank = queue[0], symbol[0]
        for move in ACTION[blank]:
            child = front.copy()

            child[blank], child[move] = child[move], child[blank]

            if child not in PATH:
                queue.append(child)
                symbol.append(move)
                MOVE.append(DIR[(blank, move)])
                PATH.append(child)

        if front == FINAL:
            break

        queue.pop(0)
        symbol.pop(0)


if __name__ == "__main__":
    node = State(BLANK, None, START, None)
    node.dfs(node)

    print("DFS: ", end='')
    node.getMoves(node)

    """
    dfs(START, BLANK)
    for step, (node, action) in enumerate(zip(PATH, MOVE)):
        print("Step #{} State: {} Move: {}".format(step, node, action))

    PATH, MOVE = [], [None]

    bfs()
    print()

    for step, (node, action) in enumerate(zip(PATH, MOVE)):
        print("Step #{} State: {} Move: {}".format(step, node, action))
    """
