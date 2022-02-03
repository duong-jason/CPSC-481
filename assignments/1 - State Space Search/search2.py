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

ACTION = [[1, 2], [0, 3], [3, 0], [2, 1]]
VISITED = []

PATH = {"route": [], "sequence": []}


def closed(state):
    """returns true if state has already been visited"""
    for item in VISITED:
        if item == state:
            return True
    return False


def dfs(state, marker):
    """depth-first search implementation"""
    VISITED.append(state.copy())
    PATH["route"].append(state.copy())

    if state != FINAL:
        for move in ACTION[marker]:
            curr = state.copy()
            curr[marker], curr[move] = curr[move], curr[marker]

            if not closed(curr):
                PATH["sequence"].append(move)
                return dfs(curr, move)

    return PATH["route"]


def bfs(state):
    """breadth-first search implementation"""
    queue, symbol = [state.copy()], [BLANK]
    VISITED.append(state.copy())

    while True:
        for move in ACTION[symbol[0]]:
            state, blank = queue[0].copy(), symbol[0]

            state[blank], state[move] = state[move], state[blank]

            if not closed(state):
                queue.append(state)
                symbol.append(move)
                PATH["sequence"].append(move)
                VISITED.append(state)

        PATH["route"].append(queue[0])

        if queue[0] == FINAL:
            break

        queue.pop(0)
        symbol.pop(0)


if __name__ == "__main__":
    dfs(START.copy(), BLANK)

    print('Moves:', PATH["sequence"])
    for depth, node in enumerate(PATH["route"]):
        print("Depth #", depth, node)

    VISITED = []
    PATH["route"] = []
    PATH["sequence"] = []
    print("\n")

    bfs(START.copy())

    print('Moves:', PATH["sequence"])
    for depth, node in enumerate(PATH["route"]):
        print("Depth #", depth, node)
