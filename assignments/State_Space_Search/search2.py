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
    (0, 1): "R",
    (0, 2): "D",
    (1, 0): "L",
    (1, 3): "D",
    (2, 3): "R",
    (2, 0): "U",
    (3, 2): "L",
    (3, 1): "U",
}

PATH = []
MOVE = [None]


def dfs(state, marker):
    """depth-first search implementation"""
    PATH.append(state)

    if state != FINAL:
        for move in ACTION[marker]:
            child = state.copy()
            child[marker], child[move] = child[move], child[marker]

            if child not in PATH:
                MOVE.append(DIR[(marker, move)])
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
    dfs(START, BLANK)
    for step, (node, action) in enumerate(zip(PATH, MOVE)):
        print("Step #{} State: {} Move: {}".format(step, node, action))

    PATH, MOVE = [], [None]

    bfs()
    print()

    for step, (node, action) in enumerate(zip(PATH, MOVE)):
        print("Step #{} State: {} Move: {}".format(step, node, action))
