#!/usr/bin/env python3
# Jason Duong
# CPSC 481-01
# 2022-02-02
# reddkingdom@csu.fullerton.edu
# @duong-jason
#
# Assignment #1
#
"""2x2 and 3x3 tile puzzle implementation with DFS and BFS"""

MARKER = 0
START, FINAL = [0, 3, 2, 1], [1, 2, 3, 0]

ACTION = [[1, 2], [0, 3], [3, 0], [2, 1]]

PATH = []
VISITED = []


def closed(state):
    """returns true if state has already been visited"""
    for item in VISITED:
        if item == state:
            return True
    return False


def dfs(state, marker):
    """depth-first search implementation"""
    VISITED.append(state.copy())
    PATH.append(state.copy())

    if state != FINAL:
        for move in ACTION[marker]:
            curr = state.copy()
            curr[marker], curr[move] = curr[move], curr[marker]

            if not closed(curr):
                return dfs(curr, move)

    return PATH


def bfs(state):
    """breadth-first search implementation"""
    queue, symbol = [state.copy()], [MARKER]
    VISITED.append(state.copy())

    while True:
        for move in ACTION[symbol[0]]:
            state, blank = queue[0].copy(), symbol[0]

            state[blank], state[move] = state[move], state[blank]

            if not closed(state):
                VISITED.append(state)
                queue.append(state)
                symbol.append(move)

        PATH.append(queue[0])

        if queue[0] == FINAL:
            break

        queue.pop(0)
        symbol.pop(0)


if __name__ == "__main__":
    dfs(START.copy(), MARKER)

    for depth, node in enumerate(PATH):
        print("Depth #", depth, node)

    VISITED = []
    PATH = []
    print("\n")

    bfs(START.copy())

    for depth, node in enumerate(PATH):
        print("Depth #", depth, node)
