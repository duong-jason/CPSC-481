#!/usr/bin/env python3
# Jason Duong
# CPSC 481-01
# 2022-02-02
# reddkingdom@csu.fullerton.edu
# @duong-jason
#
# Assignment #1
#

marker = 0
start, final = [0, 3, 2, 1], [1, 2, 3, 0]

action = [[1, 2],
          [0, 3],
          [3, 0],
          [2, 1]]

path = []
visited = []


def closed(state):
    for node in visited:
        if node == state:
            return True
    return False


def dfs(state, marker):
    visited.append(state.copy())
    path.append(state.copy())

    if state == final:
        return path 
    else:
        for move in action[marker]:
            state[marker], state[move] = state[move], state[marker]

            if not closed(state):
                return dfs(state, move)
                path.pop()

            state[marker], state[move] = state[move], state[marker]


def bfs(state):
    q, a = [state.copy()], [marker]
    visited.append(state.copy())

    while True:
        for move in action[a[0]]:
            state, blank = q[0].copy(), a[0]

            state[blank], state[move] = state[move], state[blank]

            if not closed(state):
                visited.append(state)
                q.append(state)
                a.append(move)

        path.append(q[0])

        if q[0] == final:
            break

        q.pop(0)
        a.pop(0)


if __name__ == "__main__":
    dfs(start.copy(), marker)
    
    for d in range(len(path)):
        print('Depth #', d, path[d])

    visited = []
    path = []
    print("\n")

    bfs(start.copy())

    for d in range(len(path)):
        print('Depth #', d, path[d])
