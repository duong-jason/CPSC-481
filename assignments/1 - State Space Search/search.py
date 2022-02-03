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

path, visited = [], []

def display(state):
    print(state[0], state[1])
    print(state[2], state[3])
    print("\n")

def closed(state):
    for node in visited:
        if node == state:
            return True
    return False

def dfs(state, marker, depth):
    visited.append(state.copy())
    path.append(state.copy())

    if state == final:
        return path 
    else:
        for move in action[marker]:
            state[marker], state[move] = state[move], state[marker]

            if not closed(state):
                return dfs(state, move, depth+1)
                path.pop()

            state[marker], state[move] = state[move], state[marker]


def bfs(state, depth):
    q, a = [state.copy()], [marker]
    visited.append(state.copy())

    """
        0 3
        2 1

        3 0
        2 1

        2 3
        0 1

        3 1
        2 0

        2 3
        1 0

        3 1
        0 2

        2 0
        1 3

        0 1
        3 2

        0 2
        1 3

        1 0
        3 2

        1 2
        0 3

        1 2
        3 0
    """

    while q and q[0] != final:
        print(q)
        print('Depth #', depth)
        depth += 1

        for move in action[a[0]]:
            q[0][a[0]], q[0][move] = q[0][move], q[0][a[0]]

            if not closed(q[0]):
                visited.append(q[0].copy())
                q.append(q[0].copy())
                a.append(move)

            q[0][a[0]], q[0][move] = q[0][move], q[0][a[0]]
            
        display(q[0])
        q.pop(0)
        a.pop(0)


if __name__ == "__main__":
    print('DFS\n')

    path = dfs(start.copy(), marker, 0)
    for node in path:
        display(node)

    print('BFS\n')
    bfs(start.copy(), 0)
