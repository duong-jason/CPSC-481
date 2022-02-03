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

BLANK = 0

START, FINAL = [0, 3, 2, 1], [1, 2, 3, 0]
ACTION = [(1, 2), (0, 3), (3, 0), (2, 1)]
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

CLOSED = []
PATH = {"route": [], "move": []}


def dfs(state, marker):
    """depth-first search implementation"""
    CLOSED.append(state.copy())
    PATH["route"].append(state.copy())

    if state != FINAL:
        for move in ACTION[marker]:
            top = state.copy()
            top[marker], top[move] = top[move], top[marker]

            if top not in CLOSED:
                # PATH["move"].append(DIR[(marker, move)])
                PATH["move"].append(move)
                return dfs(top, move)

    return None


def bfs(state):
    """breadth-first search implementation"""
    queue, symbol = [state.copy()], [BLANK]
    CLOSED.append(state.copy())

    while True:
        for move in ACTION[symbol[0]]:
            state, blank = queue[0].copy(), symbol[0]

            state[blank], state[move] = state[move], state[blank]

            if state not in CLOSED:
                queue.append(state)
                symbol.append(move)
                # PATH["move"].append(DIR[(blank, move)])
                PATH["move"].append(move)
                CLOSED.append(state)

        PATH["route"].append(queue[0])

        if queue[0] == FINAL or not queue:
            break

        queue.pop(0)
        symbol.pop(0)


if __name__ == "__main__":
    # 2x2 Puzzle

    dfs(START.copy(), BLANK)
    print("Moves:", PATH["move"])
    for depth, node in enumerate(PATH["route"]):
        print("Depth #", depth, node)

    CLOSED = []
    PATH = {"route": [], "move": []}

    bfs(START.copy())

    print("\nMoves:", PATH["move"])
    for depth, node in enumerate(PATH["route"]):
        print("Depth #", depth, node)

    # 3x3 Puzzle

    CLOSED = []
    PATH = {"route": [], "move": []}

    START, FINAL = [1, 4, 3, 7, 0, 6, 5, 8, 2], [1, 2, 3, 4, 5, 6, 7, 8, 0]

    ACTION = [
        [1, 3],
        [0, 2, 4],
        [1, 5],
        [0, 4, 6],
        [1, 3, 5, 7],
        [2, 4, 8],
        [3, 7],
        [4, 6, 8],
        [5, 7],
    ]

    dfs(START.copy(), BLANK)
    print("\nMoves:", PATH["move"])
    for depth, node in enumerate(PATH["route"]):
        print("Depth #", depth, node)

    CLOSED = []
    PATH = {"route": [], "move": []}

    """
    bfs(START.copy())

    print('\nMoves:', PATH['move'])
    for depth, node in enumerate(PATH['route']):
        print("Depth #", depth, node)
    """
