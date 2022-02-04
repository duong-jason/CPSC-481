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

CLOSED = []
PATH = {"route": [], "move": [None]}


def dfs(state, marker, path):
    """depth-first search implementation"""
    CLOSED.append(state.copy())
    PATH["route"].append(state.copy())

    if state != FINAL:
        for move in ACTION[marker]:
            child = state.copy()
            child[marker], child[move] = child[move], child[marker]

            if child not in CLOSED:
                return dfs(child, move, path + [DIR[(marker, move)]])
                # return dfs(child, move, path + [move])

    return path


def bfs(state):
    """breadth-first search implementation"""
    queue, symbol = [state.copy()], [BLANK]
    CLOSED.append(state.copy())

    while queue:
        blank = symbol[0]
        for move in ACTION[blank]:
            child = queue[0].copy()

            child[blank], child[move] = child[move], child[blank]

            if child not in CLOSED:
                queue.append(child)
                symbol.append(move)
                PATH["move"].append(DIR[(blank, move)])
                # PATH['move'].append(move)
                CLOSED.append(child)

        PATH["route"].append(queue[0])

        if queue[0] == FINAL:
            break

        queue.pop(0)
        symbol.pop(0)


if __name__ == "__main__":
    # 2x2 Puzzle

    PATH["move"] = dfs(START.copy(), BLANK, [])
    for times, (node, action) in enumerate(zip(PATH["route"], PATH["move"])):
        print("Search #{} State: {} Move: {}".format(times, node, action))

    CLOSED = []
    PATH = {"route": [], "move": [None]}

    bfs(START.copy())
    print("\n")

    for times, (node, action) in enumerate(zip(PATH["route"], PATH["move"])):
        print("Search #{} State: {} Move: {}".format(times, node, action))

    """
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

    PATH["move"] = dfs(START.copy(), BLANK, [])
    print("Moves:", PATH["move"])
    for depth, node in enumerate(PATH["route"]):
        print("Depth #", depth, node)

    CLOSED = []
    PATH = {"route": [], "move": []}

    bfs(START.copy())

    print("\nMoves:", PATH["move"])
    for depth, node in enumerate(PATH["route"]):
        print("Depth #", depth, node)
    """
