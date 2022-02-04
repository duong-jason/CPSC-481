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
                MOVE.append([move])
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
                MOVE.append(move)
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
